from flask import request
from flask import jsonify
from flask import Blueprint
from jsonschema import exceptions
from jsonschema import validate

from server.app import db
from .schemas import *

import hashlib

user_api = Blueprint("user_api", __name__)


def validate_json(schema, data):
    try:
        validate(instance=data, schema=schema)
    except exceptions.ValidationError as e:
        print(e)
        return False
    return True


def user_object(user, password=False):
    user_obj = {
        "id_user":      user[0],
        "first_name":   user[1],
        "last_name":    user[2],
        "email":        user[3],
    }
    if password:
        user_obj["password"] = user[4]
    return user_obj


@user_api.route("/register", methods=["POST"])
def create():
    """
    Create user function
    """

    data = request.json["properties"]

    # validation of the received data
    if not validate_json(create_schema, data):
        return jsonify({"error": "Data is invalid"}), 400

    # search users with the same email address
    temp = db.select_rows(
        f"select * from account where email='{data['email']}'"
    )

    if temp is not None:
        return jsonify(
            {"error": "User with this email addres already exists"}
        ), 400

    db.insert_data(
        f"""
        insert into account (first_name, last_name, email, password) values (
            '{data["first_name"]}', 
            '{data["last_name"]}', 
            '{data["email"]}',  
            '{hashlib.md5(data["password"].encode()).hexdigest()}'
        )"""
    )
    db.commit()

    response = {
        "result": "ok"
    }
    return jsonify(response), 400


@user_api.route("/login", methods=["GET"])
def login():
    """
    Login user function
    """
    data = request.json["properties"]

    # validation of the received data
    if not validate_json(login_schema, data):
        return jsonify({"error": "Data is invalid"}), 400

    # search user by email
    user = db.select_rows(
        f"select * from account where email='{data['email']}'"
    )[0]

    if user is None:
        return jsonify(
            {"error": "User with this email addres not exists"}
        ), 400

    if user[-1] != hashlib.md5(data["password"].encode()).hexdigest():
        return jsonify(
            {"error": "Incorrect password"}
        ), 400

    response = {
        "result": "ok",
        "user": user_object(user),
    }
    return jsonify(response), 200




