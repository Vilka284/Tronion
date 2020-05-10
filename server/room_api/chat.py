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


def get_messages_story(room_id):
    """
    Get the last 200(u can change this value if u want) messages by room id.
    Messages sorted by send date
    """
    messages = db.select_rows(f"""
        select content, date_send, user_id from
        message inner join room on
        room.id_room = message.room_id
        where room.id_room = {int(room_id)}
        order by date_send desc limit 200;
    """)

    response = []
    if messages is not None:
        for item in messages:
            response.append({
                    "user": item[2],
                    "data": item[0],
                    "send_on": item[1].strftime("%H:%M")
                }
            )
    return response



@Auth.login_required
@sio.on('join')
def handle_join(data):
    response = get_messages_story(data["room"])
    join_room(data["room"])
    emit('response', response, room=data["room"])



@Auth.login_required
@sio.on('my_room_event')
def send_room_message(message):
    print(message)
    if message["data"]:
        send_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(send_on)
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
        response = [{
                "user": get_user_by_id(message["user"]).upper(),
                "data": message['data'],
                "send_on": send_on
            }
        ]

        emit('response', response, room=message["room"])






