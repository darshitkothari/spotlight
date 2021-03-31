from app.main import db
from app.main.models.department import Department
from app.main.models.user import User
import re


class DepartmentHelper:
    @staticmethod
    def save_new_department(data):
        department_name = '_'.join(re.sub("[^a-zA-Z0-9 \n.]", '', data['name']).split()).upper()
        department = Department.query.filter_by(name=department_name).first()
        if not department:
            user = User.query.filter_by(unique_id=data['fk_user_id']).first()
            if not user:
                response_object = {'status': 'failure', 'message': 'user does not exist'}
                return response_object, 404
            else:
                new_department = Department(name=department_name, fk_user_id=data['fk_user_id'])
                db.session.add(new_department)
                db.session.commit()
                response_object = {'status': 'success', 'message': 'department added successfully!'}
                return response_object, 201
        else:
            response_object = {'status': 'failure', 'message': 'department already exists.'}
            return response_object, 409

    @staticmethod
    def get_department_by_id(department_id):
        return Department.query.filter_by(id=department_id).first()

    @staticmethod
    def get_all_departments():
        return Department.query.all()

    @staticmethod
    def update_department(department_id, data):
        department = Department.query.filter_by(id=department_id).first()
        if not department:
            response_object = {'status': 'failure', 'message': 'department does not exist!'}
            return response_object, 404
        else:
            for key, val in data.items():
                if key not in ['created_on', 'updated_on', 'fk_user_id']:
                    pass
                else:
                    response_object = {'status': 'failure', 'message': 'cannot update system fields'}
                    return response_object, 405

    @staticmethod
    def delete_department(department_id):
        department = Department.query.filter_by(id=department_id).first()
        if not department:
            response_object = {'status': 'failure', 'message': 'department does not exist!'}
            return response_object, 404
        else:
            Department.query.filter_by(id=department_id).delete()
            db.session.commit()
            response_object = {'status': 'success', 'message': 'department deleted successfully!'}
            return response_object, 204
