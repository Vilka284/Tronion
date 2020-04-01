from flask import Blueprint
from server.user_auth.api import UserApi

user_auth = Blueprint("user_auth", __name__)

user_view = UserApi.as_view("user_api")
user_auth.add_url_rule("/user", methods=["POST"], view_func=user_view)
user_auth.add_url_rule(
    "/user/<int:id>",
    methods=['GET', 'PUT', 'DELETE'],
    view_func=user_view,
)
