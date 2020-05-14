from server.app import db


def get_user_rooms(id_user):
    """
    Get rooms by user id

    :param id_user:
    :return: rooms
    """
    rooms = []
    user_room = db.select_rows(
        f"select * from room_has_user where user_id = {id_user} and user_status_id = 1"
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