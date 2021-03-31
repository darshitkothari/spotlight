from app.main import db
from app.main.models.policy import Policy
from app.main.models.user import User
import re


class PolicyHelper:
    @staticmethod
    def save_new_policy(data):
        pass

    @staticmethod
    def get_policy_by_id(policy_id):
        return Policy.query.filter_by(id=policy_id).first()

    @staticmethod
    def get_all_policies():
        return Policy.query.all()

    @staticmethod
    def update_policy(policy_id):
        pass

    @staticmethod
    def delete_policy(policy_id):
        policy = Policy.query.filter_by(id=policy_id).first()
        if not policy:
            response_object = {'status': 'failure', 'message': 'policy does not exist!'}
            return response_object, 404
        else:
            Policy.query.filter_by(id=policy_id).delete()
            db.session.commit()
            response_object = {'status': 'success', 'message': 'policy deleted successfully!'}
            return response_object, 204
