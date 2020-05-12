from flask import render_template, request,\
    redirect, url_for, Blueprint
from flask_login import login_user, logout_user,\
    login_required, current_user
from app.main.services.user_service import UserHelper

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
        users = UserHelper.get_all_users()
        return render_template('admin/users.html', data=users)


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
