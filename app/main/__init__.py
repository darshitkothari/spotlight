from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from .config import config_by_name

# Creating Extensions
db = SQLAlchemy()
login_manager = LoginManager()
flask_bcrypt = Bcrypt()


# Create app function based on the paramter from config_by_name and returns app instance
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    login_manager.init_app(app)
    flask_bcrypt.init_app(app)
    return app
