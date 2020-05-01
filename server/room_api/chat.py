from flask_socketio import Namespace
from flask_socketio import leave_room
from flask_socketio import join_room
from flask_socketio import emit
from flask import request, jsonify, g


from .endpoints import room_api

from server.app import db
from server.app import sio
from server.user_api.endpoints import validate_json
from server.auth_jwt import Auth
from .schemas import *

from datetime import datetime


def get_user_by_id(id):
    return " ".join(db.select_rows(
        f"select first_name, last_name from account where id_user={int(id)}"
    )[0])


@Auth.login_required
@sio.on('my_room_event')
def send_room_message(message):
    if message["data"]:
        send_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # datetime.now().strftime("%H:%M")

        db.insert_data(
            f"""
                insert into message(content, date_send, room_id, user_id) 
                values (
                    '{message["data"]}',
                    '{send_on}',
                    {int(message["room"])},
                    {int(message["user"])}
                )           
                
            """
        )
        db.commit()

        response = {
            "user": get_user_by_id(message["user"]).upper(),
            "data": message['data'],
            "send_on": send_on,

        }

        emit('response', response, room=message["room"])



@Auth.login_required
@sio.on('join')
def handle_join(data):
    join_room(data["room"])





