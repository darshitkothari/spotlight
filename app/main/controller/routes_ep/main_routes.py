from flask import render_template, request,\
    redirect, url_for, Blueprint
from flask_login import login_user, logout_user,\
    login_required, current_user

# Defining main related route Blueprint: 'main'
main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    return render_template("main/main_index.html")
