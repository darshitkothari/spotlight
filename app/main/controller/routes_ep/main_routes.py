from flask import render_template, request,\
    redirect, url_for, Blueprint
from flask_login import login_user, logout_user,\
    login_required, current_user

# Defining main related route Blueprint: 'main'
main = Blueprint('main', __name__)


@main.route('/index')
@login_required
def main_index():
    return render_template("main/main_index.html")


@main.route('/ui-profile')
@login_required
def usr_profile():
    return render_template("main/user_profile.html")
