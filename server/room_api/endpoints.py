from flask import session
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify
from flask import Blueprint
from jsonschema import exceptions
from jsonschema import validate

from functools import wraps

from server.app import db


room_api = Blueprint("room_api", __name__)


@room_api.route("/create-room", methods=["POST"])
def create_room():
    return jsonify({"resp": "hi!"})