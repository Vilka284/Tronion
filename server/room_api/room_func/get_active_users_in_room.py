from server.app import db
from server.room_api.room_func.get_user_rooms import get_user_rooms


# check if user admin of room
def check_admin(admin_id, code):
    rooms, message = get_user_rooms(id_user=admin_id)
    print('rooms:', rooms,'message:', message)
    for room in rooms:
        if room[0] == code:
            return True
    else:
        return False


# get active users
def get_active_users_in_room(admin_id, code):
    if check_admin(admin_id=admin_id, code=code):
        # user_status_id: 1 - admin, 2 - user
        users = db.select_rows(
                f"""select * from room_has_user 
                    where (room_id = {code}) and 
                            (user_status_id = 2)"""
        )
        return users
    return 0
