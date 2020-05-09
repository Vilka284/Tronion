from flask import request
from flask import jsonify
from flask import Blueprint
from flask import g
from flask_socketio import join_room as jr

from random import randrange

from server.app import db, sio
from server.user_api.endpoints import validate_json
from server.auth_jwt import Auth
from .schemas import *


room_api = Blueprint("room_api", __name__)

from .chat import handle_join, send_room_message


def get_room(code):
    """
    Get room by code

    :param code: room code
    :return: room
    """
    room = db.select_rows(
        f"select * from room where id_room = {code}"
    )
    return room


def rand_code():
    """
    Generation of five character id

    :return: random code
    """
    code = str(randrange(10000, 99999))
    if get_room(code) is None:
        return code
    return rand_code()



def get_user_rooms(id_user):
    """
    Get rooms by user id

    :param id_user:
    :return: rooms
    """
    rooms = []
    user_room = db.select_rows(
        f"select * from room_has_user where user_id = {id_user}"
    )
    if user_room is not None:
        message = 'Here is your rooms:'
        for room in user_room:
            rooms.extend(db.select_rows(
                f"select * from room where id_room = {room[1]}"
            ))
    else:
        message = 'You have no rooms! Do you want to create one?'
    return rooms, message


# @room_api.route('/update_info', methods=["GET", "POST"])
# def update_info():
#     return jsonify({"message": "its work!"})


@room_api.route('/create_room', methods=["POST"])
@Auth.login_required
def create_room():
    """
    Create room function

    :return:
    """

    data = request.json

    # validation of the received data
    if not validate_json(data, room_create_schema):
        return jsonify({"error": "Data is invalid"}), 400

    code = rand_code()
    print(data)
    try:
        db.insert_data(
            f"""
                    insert into room (id_room, name_room, note) values (
                       '{code}', 
                       '{data['name']}', 
                       '{data['description']}'
                    )"""
        )
        db.commit()

        # Давайте наступного разу називати конкретно id_вещь, або вещь_id
        # Інакше запутатись можна
        db.insert_data(
            f"""
                    insert into room_has_user (user_id, room_id) values ( 
                           '{data['id_user']}', 
                           '{code}'
                       )"""
        )
        db.commit()
    except:
        from sys import exc_info
        print(exc_info()[0])
        return jsonify({"error": "Catch DB exception"}), 400

    response = {
        "result": "ok"
    }

    return jsonify(response), 200


@room_api.route("/update_manage", methods=["POST"])
@Auth.login_required
def update_manage():
    """

    Update manage room info
    :return:
    """
    data = request.json
    print(request.headers)
    rooms, message = get_user_rooms(data["id_user"])

    print(rooms)

    response = {
        "message": message,
        "rooms": rooms
    }

    return jsonify(response), 200


@room_api.route("/join_room", methods=["POST"])
@Auth.login_required
def join_room():
    """
    Join room function

    :return:
    """


    print(g.user["user_id"])
    # print(req)
    # print(request.sid)
    # join_room(req.sid, 10219)
    data = request.json
    code = data['code']
    print(request.headers)

    db_data = db.select_rows(
        f"select * from room where id_room = {code}"
    )

    if db_data is None:
        return jsonify({"error": "There is no room with this code"}), 404


    response = {
        "result": "ok",
        "room_data": db_data[0]
    }
    return jsonify(response), 200


@room_api.route("/test", methods=["GET"])
@Auth.login_required
def test():
    return jsonify({"message": "its work!"})
