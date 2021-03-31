from flask import render_template, request,\
    redirect, url_for, Blueprint
from flask_login import login_user, logout_user,\
    login_required, current_user
import requests
from ...services.user_service import UserHelper
from os import environ

# Defining main related route Blueprint: 'main'
admin = Blueprint('admin', __name__)

# Fetch & Set App Uri
app_uri = environ.get("APP_URI")


@admin.route('/admin')
@login_required
def admin_index():
    if current_user.is_admin:
        return render_template('admin/admin_index.html')


@admin.route('/admin/ui-users')
@login_required
def ui_users():
    if current_user.is_admin:
        users = requests.get(app_uri + "/rest/api/v1/user", verify=False).json()['data']
        return render_template('admin/ui_users.html', data=users, len=len(users))


@admin.route('/admin/ui-users/<user_id>')
@login_required
def ui_user_info(user_id):
    if current_user.is_admin:
        user = UserHelper.get_user(user_id)
        if not user:
            return render_template('error')
        print(user_id)
        return render_template('admin/ui_user_info.html')


@admin.route('/admin/ui-policies')
@login_required
def ui_policies():
    if current_user.is_admin:
        return render_template('admin/ui_policies.html')


@admin.route('/admin/ui-trainings')
@login_required
def ui_trainings():
    if current_user.is_admin:
        return render_template('admin/ui_trainings.html')


@admin.route('/admin/ui-profile')
@login_required
def adm_profile():
    if current_user.is_admin:
        return render_template('admin/admin_profile.html')
