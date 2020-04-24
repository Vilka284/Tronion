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


@room_api.route('/create_room', methods=["POST"])
def create_room():

    def rand_code():
        from random import randrange
        return str(randrange(10000, 99999))

    def check():
        code = rand_code()
        temp = db.select_rows(
            f"select * from room where id_room like {code}"
        )
        if temp is not None:
            check()
        else:
            return code

    data = request.json
    print(data)
    code = check()
    print(code)

    db.insert_data(
        f"""
            insert into room (id_room, name_room, note) values (
                   '{code}', 
                   '{data["name"]}', 
                   '{data["description"]}'
               )"""
        )
    db.commit()

    response = {
        "result": "ok"
    }
    return jsonify(response), 200