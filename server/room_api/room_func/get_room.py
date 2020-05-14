from random import randrange

from server.app import db


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