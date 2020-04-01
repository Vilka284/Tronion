from flask.views import MethodView
from flask import jsonify, request


UserData = {
    1: {
        "name": "roman",
        "surname": "bliakhar",
        "email_address": "bliakharr@gmail.com",
        "password": "1111"
    },
    2: {
        "name": "andrew",
        "surname": "syd",
        "email_address": "viilka284@gmail.com",
        "password": "1111"
    },
    3: {
        "name": "danylo",
        "surname": "mashtalir",
        "email_address": "danylo5202@gmail.com",
        "password": "1111"
    },
    "counter": 3
}

error = {
    "UserNotFound": {
        "message": "User not found"
    }
}


class UserApi(MethodView):

    def get(self, id):
        if id in UserData.keys():
            return jsonify(UserData[id]), 200
        return jsonify(error["UserNotFound"]), 400

    def post(self):
        UserData["counter"] += 1
        body = request.get_json()
        UserData[UserData["counter"]] = {
            "name": body.get("name"),
            "surname": body.get("surname"),
            "email_address": body.get("email_address"),
        }
        return jsonify(UserData[UserData["counter"]]), 200

    def put(self, id):
        if id in UserData.keys():
            body = request.get_json()
            UserData[id] = {
                "name": body.get("name"),
                "surname": body.get("surname"),
                "email_address": body.get("email_address"),
            }
            return jsonify(UserData[id]), 200
        return jsonify(error["UserNotFound"]), 400

    def delete(self, id):
        if id in UserData.keys():
            del UserData[id]
            return {"message": "User deleted"}
        return jsonify(error["UserNotFound"]), 400

