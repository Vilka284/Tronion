from flask import Flask, render_template
from config import Config
from os import path, getcwd

# setting up app name and templates directory
app = Flask(__name__, template_folder= path.abspath(getcwd()) + '/client/templates')

def create_app():

    # load config
    app.config.from_object(Config)

    from server.user_auth.urls import user_auth

    # reg blueprints
    app.register_blueprint(user_auth)
    return app

