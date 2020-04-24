from flask import Flask, render_template
from config import Config
from os import path, getcwd
from db import Databse


# setting up app name and templates directory
TEMPLATE_DIR = path.abspath(getcwd()) + '/client/templates'
STATIC_DIR = path.abspath(getcwd()) + '/client/static/'

app = Flask(__name__,
            template_folder=TEMPLATE_DIR,
            static_folder=STATIC_DIR)

# connect to database
db = Databse()
db.connection()



def create_app():

    # load config
    app.config.from_object(Config)

    from server.user_api.endpoints import user_api
    from server import routes
    # reg blueprints
    app.register_blueprint(user_api)

    return app

