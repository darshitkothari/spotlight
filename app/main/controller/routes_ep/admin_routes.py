from flask import render_template, request,\
    redirect, url_for, Blueprint
from flask_login import login_user, logout_user,\
    login_required, current_user
from app.main.services.user_service import UserHelper
from app.main.controller.api_ep.user_api import UserList
import requests

# Defining main related route Blueprint: 'main'
admin = Blueprint('admin', __name__)


@admin.route('/admin')
@login_required
def admin_index():
    if current_user.is_admin:
        return render_template('admin/admin_index.html')


@admin.route('/admin/ui-users')
@login_required
def ui_users():
    if current_user.is_admin:
        users = requests.get('https://ahwspl.policy.com:5000/rest/api/v1/user', verify=False).json()['data']
        return render_template('admin/users.html', data=users, len=len(users))


@admin.route('/admin/ui-policies')
@login_required
def ui_policies():
    if current_user.is_admin:
        return render_template('admin/policies.html')


@admin.route('/admin/ui-trainings')
@login_required
def ui_trainings():
    if current_user.is_admin:
        return render_template('admin/trainings.html')
