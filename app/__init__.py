from flask_restplus import Api
from flask import Blueprint
import os
from dotenv import load_dotenv

# Loading Environment variables
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top root folder
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

# Creating blueprint for api endpoint
blueprint = Blueprint('api', __name__, url_prefix='/rest/api/v1')
