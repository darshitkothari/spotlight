from flask import request
from flask_restplus import Resource
from ...util.dto import UserDto
from ...services.user_service import UserHelper
# from app.main.util.decorator import token_required


api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """ list all registered users """
        return UserHelper.get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """ Creates a new User """
        data = request.json
        return UserHelper.save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, unique_id):
        """ get a user given its identifier """
        user = UserHelper.get_user(unique_id)
        if not user:
            api.abort(404)
        else:
            return user

    @api.expect(_user)
    @api.response(204, 'User successfully updated.')
    @api.doc('update a user')
    def put(self):
        """ update a user given its identifier """
        return "Hello"

    @api.doc('delete a user')
    @api.response(204, 'User successfully deleted.')
    def delete(self, unique_id):
        """ delete a user given its identifier """
        return UserHelper.delete_user(unique_id)
