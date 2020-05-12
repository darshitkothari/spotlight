from flask import render_template, request,\
    redirect, url_for, Blueprint
from app.main import login_manager
from flask_login import login_user, logout_user,\
    login_required, current_user
import json
import requests
import os
from app.main.models.user import User
from oauthlib.oauth2 import WebApplicationClient
import datetime
from app.main.services.user_service import UserHelper

# Defining auth related route Blueprint: 'auth'
auth = Blueprint('auth', __name__)

# OAuth2 client setup
client = WebApplicationClient(os.getenv("GOOGLE_CLIENT_ID"))


@login_manager.user_loader
def load_user(unique_id):
    """
        Given *user_id*, return the associated User object.
        :param unicode unique_id: user_id (email) user to retrieve
    """
    return User.query.get(unique_id)


@auth.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.main_index'))
    else:
        # Find out what URL to hit for Google login
        google_provider_cfg = get_google_provider_cfg()
        authorization_endpoint = google_provider_cfg["authorization_endpoint"]

        # Use library to construct the request for login and provide
        # scopes that let you retrieve user's profile from Google
        request_uri = client.prepare_request_uri(authorization_endpoint, redirect_uri=request.base_url + "/callback",
                                                 scope=["openid", "email", "profile"],)
        return redirect(request_uri)


@auth.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(token_endpoint, authorization_response=request.url,
                                                            redirect_url=request.base_url, code=code,)
    token_response = requests.post(token_url, headers=headers, data=body, auth=(os.getenv("GOOGLE_CLIENT_ID"),
                                                                                os.getenv("GOOGLE_CLIENT_SECRET"),))

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that we have tokens (yay) let's find and hit URL from Google that gives you user's profile information,
    # including their Google Profile Image and Email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # We want to make sure their email is verified. The user authenticated with Google, authorized our app, and now
    # we've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["name"]
    else:
        return "User email not available or not verified by Google.", 400
    # Create a user in our db with the information provided by Google
    data = {"unique_id": unique_id, "name": users_name, "email": users_email, "profile_pic": picture}
    UserHelper.save_new_user(data=data)

    # Begin user session by logging the user in
    login_user(User.query.get(data['unique_id']))
    # Send user back to homepage
    return redirect(url_for("main.main_index"))


@login_manager.unauthorized_handler
def unauthorized():
    return render_template("auth/signin.html")
    # return "You must be logged in to access this content.", 403


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.main_index"))


def get_google_provider_cfg():
    return requests.get(os.getenv("GOOGLE_DISCOVERY_URL")).json()
