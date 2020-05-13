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


def is_join(room_id, user_id):
    temp = db.select_rows(
        f"""
        select * from  room_has_user 
        where room_id={int(room_id)} and user_id={int(user_id)} 
        """
    )
    return temp
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
                    insert into room_has_user (user_id, room_id, user_status_id) values ( 
                           '{data['id_user']}', 
                           '{code}',
                           1 
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
    rooms, message = get_user_rooms(data["id_user"])
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
    """

    data = request.json
    print(data)
    code = data["code"]
    user = data["user_id"]

    db_data = db.select_rows(
        f"select * from room where id_room = {code};"
    )

    # check
    if is_join(code, user) is None:
        db.insert_data(
            # user_status_id: 1 - admin, 2 - moderator, 3 - user
            f"""
            insert into room_has_user (user_id, room_id, user_status_id)
            values ({int(user)}, {int(code)}, 3)
            """
        )


    # **приклад запиту**
    # temp = db.select_rows(
    #     """
    #     select status.status_name from
    #     account inner join room_has_user on account.id_user = room_has_user.user_id
    #     inner join room on room_has_user.room_id = room.id_room
    #     inner join status on room_has_user.user_status_id = status.id_status
    #     where account.id_user = {тут маэ бути ід юзера};
    #     """
    # )

    if db_data is None:
        return jsonify({"error": "There is no room with this code"}), 404



    response = {
        "result": "ok",
        "room_data": db_data[0]
    }
    return jsonify(response), 200


@room_api.route("/user_in_room", methods=["POST"])
@Auth.login_required
def user_in_room():

    data = request.json
    user_id = data['id_user']
    is_in_room = data['is_in_room']

    if is_in_room is 1:
        pass
    else:
        pass

    response = {
        "result": "ok"
    }
    return jsonify(response)



@room_api.route("/test", methods=["GET"])
@Auth.login_required
def test():
    return jsonify({"message": "its work!"})
