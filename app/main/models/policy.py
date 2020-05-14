from ..import db


class Policy(db.Model):
    """ Policy Model for storing policy related details """
    __tablename__ = "policy"

    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.String(255), unique=True, nullable=False)
    fk_department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    file_loc = db.Column(db.Text, nullable=False)
    fk_author_id = db.Column(db.String(100), db.ForeignKey('user.unique_id'), nullable=False)
    version = db.Column(db.Integer, nullable=False, default=1)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    is_active = db.Column(db.Boolean, nullable=False, default=True)
