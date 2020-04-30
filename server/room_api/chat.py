from flask_socketio import Namespace
from flask_socketio import leave_room
from flask_socketio import join_room
from flask import request, jsonify


from .endpoints import room_api

from server.app import db
from server.app import sio
from server.user_api.endpoints import validate_json
from server.auth_jwt import Auth
from .schemas import *



@room_api.route("/create_chat", methods=["POST"])
@Auth.login_required
def create_chat():
    """
    Create chat function
    """

    data = request.json

    # validation of the received data
    if not validate_json(data, chat_create_shcema):
        return jsonify({"error": "Data is invalid"}), 400

    # search room by id
    room = db.select_rows(
        f"select * from room where id_room={data['room_id']}"
    )[0]
    if room is None:
        return jsonify(
            {"error": "Room with this id not exists"}
        ), 400

    db.insert_data(
        f"""
             insert into chat (name, description, room_id) values (
                    '{data['name']}', 
                    '{data['description']}',
                    {data['room_id']}
                )"""
    )
    db.commit()

    response = {
        "result": "ok"
    }
    return jsonify(response), 200



# @sio.


