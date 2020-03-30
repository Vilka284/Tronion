from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)

    # load config
    app.config.from_object(Config)

    from server.user_auth.urls import user_auth

    # reg blueprints
    app.register_blueprint(user_auth)
    return app
