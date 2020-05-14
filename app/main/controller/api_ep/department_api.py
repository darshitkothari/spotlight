from flask import request
from flask_restplus import Resource
from ...util.dto import DepartmentDto
from ...services.department_service import DepartmentHelper


api = DepartmentDto.api
_department = DepartmentDto.department


@api.route('/')
class DepartmentList(Resource):
    @api.doc('list_of_departments')
    @api.marshal_list_with(_department, envelope='data')
    def get(self):
        """ list all departments """
        return DepartmentHelper.get_all_departments()

    @api.response(201, 'Department successfully created.')
    @api.doc('create a new department')
    @api.expect(_department, validate=True)
    def post(self):
        """ Creates a new department """
        data = request.json
        return DepartmentHelper.save_new_department(data=data)


@api.route('/<id>')
@api.param('id', 'The Department identifier')
@api.response(404, 'Department not found.')
class Department(Resource):
    @api.doc('get a department')
    @api.marshal_with(_department)
    def get(self, department_id):
        """ get a department given its identifier """
        department = DepartmentHelper.get_department_by_id(department_id)
        if not department:
            api.abort(404)
        else:
            return department

    @api.expect(_department)
    @api.response(204, 'Department successfully updated.')
    @api.doc('update a department')
    def put(self):
        """ update a department given its identifier """
        return "Hello"

    @api.doc('delete a department')
    @api.response(204, 'Department successfully deleted.')
    def delete(self, department_id):
        """ delete a department given its identifier """
        return DepartmentHelper.delete_department(department_id)
