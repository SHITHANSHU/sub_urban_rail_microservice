from flask import Flask
from .config import app_config
from .view.rail_view import rail_api as rail_blueprint
import os


def create_app(env_name):
    app=Flask(__name__)
    app.config.from_object(app_config[env_name])
    # print("creating task")
    # print(app_config[env_name].DEBUG)
    # print(os.getenv('DEV_DATABASE_URL'))


    app.register_blueprint(rail_blueprint,url_prefix="/api/v1/rail")
    
    return app
