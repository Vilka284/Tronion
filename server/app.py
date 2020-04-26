from flask import Flask, render_template
from config import Config
from os import path, getcwd
from db import Databse
from flask_socketio import SocketIO


# setting up app name and templates directory
TEMPLATE_DIR = path.abspath(getcwd()) + '/client/templates'
STATIC_DIR = path.abspath(getcwd()) + '/client/static/'

app = Flask(__name__,
            template_folder=TEMPLATE_DIR,

            static_folder=STATIC_DIR)
# load config
app.config.from_object(Config)

sio = SocketIO(app)

# connect to database
db = Databse()
db.connection()


def create_app():
    from server.user_api.endpoints import user_api
    from server.room_api.endpoints import room_api

    # reg blueprints
    app.register_blueprint(user_api)
    app.register_blueprint(room_api)

    from server import routes
    # reg blueprints
    app.register_blueprint(user_api)

    return app

