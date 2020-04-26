from flask import request
from flask import jsonify
from flask import Blueprint

from random import randrange

from server.app import db
from server.user_api.endpoints import validate_json
from server.auth_jwt import *
from .schemas import *

room_api = Blueprint("room_api", __name__)


def get_room(code):
    temp = db.select_rows(
        f"select * from room where id_room = {code}"
    )
    return temp


def rand_code():
    """
    Generation of five character id
    """
    code = str(randrange(10000, 99999))
    if get_room(code) is None:
        return code
    return rand_code()


@room_api.route('/create_room', methods=["POST"])
@Auth.login_required
def create_room():
    """

    Create room function
    """

    data = request.json
    print(data)

    # validation of the received data
    if not validate_json(data, room_create_schema):
        return jsonify({"error": "Data is invalid"}), 400

    code = rand_code()

    db.insert_data(
        f"""
            insert into room (id_room, name_room, note) values (
                   '{code}', 
                   '{data['name']}', 
                   '{data['description']}'
               )"""
        )
    db.commit()

    response = {
        "result": "ok"
    }
    return jsonify(response), 200

@room_api.route('/update_info', methods=["GET", "POST"])
def update_info():
    return jsonify({"message": "its work!"})

@room_api.route("/test", methods=["GET"])
@Auth.login_required
def test():
    return jsonify({"message": "its work!"})

