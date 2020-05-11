from flask import Flask
from config import Config
from os import path, getcwd
from db import Databse
from flask_socketio import SocketIO

import os

# setting up app name and templates directory
TEMPLATE_DIR = path.abspath(getcwd()) + '/client/templates'
STATIC_DIR = path.abspath(getcwd()) + '/client/static/'

app = Flask(__name__,
            template_folder=TEMPLATE_DIR,
            static_folder=STATIC_DIR)

# load config
app.config.from_object(Config)
app.config['POLLS_VOTE_URL'] = os.environ.get('POLLS_VOTE_URL')

sio = SocketIO(app)

# connect to database
db = Databse()
db.connection()


def create_app():
    from server.user_api.endpoints import user_api
    from server.room_api.endpoints import room_api
    from server.poll_api.endpoints import poll_api

    from server import routes
    # reg blueprints
    app.register_blueprint(user_api)
    app.register_blueprint(room_api)
    app.register_blueprint(poll_api, url_prefix='/polls')

    return app
