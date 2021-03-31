from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'unique_id': fields.String(required=False, description='user identifier'),
        'name': fields.String(required=True, description='user full name'),
        'email': fields.String(required=True, description='user email address'),
        'admin': fields.Boolean(required=False, description='user role'),
        'created_on': fields.DateTime(required=False, description='user creation timestamp'),
        # 'is_active': fields.Boolean(required=False, description='user status')
    })


class DepartmentDto:
    api = Namespace('department', description='department related operations')
    department = api.model('department', {
        'id': fields.Integer(required=False, description='department identifier'),
        'name': fields.String(required=True, description='department name'),
        'fk_user_id': fields.String(required=True, description='user id'),
        'created_on': fields.DateTime(required=False, description='user creation timestamp'),
        'is_active': fields.Boolean(required=False, description='department status'),
    })


class PolicyDto:
    api = Namespace('policy', description='policy related operations')
    policy = api.model('policy', {
        'id':  fields.Integer(required=False, description='policy identifier'),
        'title': fields.String(required=True, description='policy title'),
        'fk_department_id': fields.Integer(required=False, description='department identifier'),
    })
