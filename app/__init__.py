from flask_restplus import Api
from flask import Blueprint
import os
from dotenv import load_dotenv
from .main.controller.api_ep.user_api import api as user_ns
from .main.controller.api_ep.department_api import api as dept_ns

# Loading Environment variables
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top root folder
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

# Creating blueprint for api endpoint
blueprint = Blueprint('api', __name__, url_prefix='/rest/api/v1')
api = Api(blueprint, version=1.0, title='Spotlight Rest Apis',
          description='Created Flask-Restplus powered Api used for generic purpose')

# Registering namespace
api.add_namespace(user_ns)
api.add_namespace(dept_ns)
