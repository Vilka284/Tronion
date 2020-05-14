from server.app import db


def is_join(room_id, user_id):
    temp = db.select_rows(
        f"""
        select * from  room_has_user 
        where room_id={int(room_id)} and user_id={int(user_id)} 
        """
    )
    return temp