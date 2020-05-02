from ..import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """ User Model for storing user related details """
    __tablename__ = "user"

    unique_id = db.Column(db.String(100), unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    department = db.Column(db.Text, nullable=True)
    designation = db.Column(db.Text, nullable=True)
    profile_pic = db.Column(db.Text, nullable=True)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    # UserMixin Methods
    def is_active(self):
        """ True, as all users are active. """
        return True

    def get_id(self):
        """ Returns user public id """
        return self.unique_id

    def is_authenticated(self):
        """ Return True if the user is authenticated. """
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def __repr__(self):
        return "<User '{}'>".format(self.email)
