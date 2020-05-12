from app.main import db
from app.main.models.user import User


class UserHelper:
    @staticmethod
    def save_new_user(data):
        user = User.query.filter_by(unique_id=data['unique_id']).first()
        if not user:
            new_user = User(unique_id=data['unique_id'], name=data['name'], email=data['email'],
                            profile_pic=data['profile_pic'])
            db.session.add(new_user)
            db.session.commit()
            response_object = {'status': 'success', 'message': 'user registered successfully!'}
            return response_object, 201
        else:
            response_object = {'status': 'failure', 'message': 'user already exists. please log in!'}
            return response_object, 409

    @staticmethod
    def get_user(unique_id):
        return User.query.filter_by(unique_id=unique_id).first()

    @staticmethod
    def get_all_users():
        return User.query.all()
