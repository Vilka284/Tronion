from flask import jsonify, url_for, redirect, render_template
from flask import request
from flask import g
from config import Config

import jwt

from functools import wraps
import datetime


class Auth:
    """
    Auth class
    """

    @staticmethod
    def auth_token(user_id):
        """
        Generates the Auth Token
        """

        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload=payload,
                key=Config.SECRET_KEY,
                algorithm="HS256",
            ).decode("utf-8")
        except Exception as e:
            return jsonify({'error': 'error in generating user token'}), 400


    @staticmethod
    def login_required(func):
        """
        Auth decorator
        """

        @wraps(func)
        def decorator(*args, **kwargs):

            if "auth_token" not in request.headers:
                return {"error": "token is missing"}, 400
                #return redirect(url_for('login')), 400
                #render_template('login/login.html')

            user_id = None

            token = request.headers["auth_token"]
            # decode token
            try:
                payload = jwt.decode(token, Config.SECRET_KEY)
                user_id = payload["sub"]
            except jwt.ExpiredSignatureError as e:
                return {'message': 'token expired'}, 400
                #return redirect(url_for('login')), 400
            except jwt.InvalidTokenError as e:
                return {'message': 'Invalid token, please try again'}, 400


            g.user = {"user_id": user_id}
            return func(*args, **kwargs)
        return decorator









