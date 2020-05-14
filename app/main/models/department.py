from ..import db


class Department(db.Model):
    """ Department Model for storing department related details """
    __tablename__ = "department"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    fk_user_id = db.Column(db.String(100), db.ForeignKey('user.unique_id'), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    policy = db.relationship('Policy', backref='department', lazy=True)
