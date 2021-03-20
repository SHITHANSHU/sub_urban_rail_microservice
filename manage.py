import os
from flask_script import Manager
from src.app import create_app
from dotenv import load_dotenv
import logging



load_dotenv()
env_name=os.getenv('FLASK_ENV')
app=create_app(env_name)
manager = Manager(app=app)


if __name__ == "__main__":
    logging.basicConfig(filename='system.log')
    manager.run()