room_create_schema = {
    "name": {"type": "string"},
    "description": {"type": "string"},
}


chat_create_shcema = {
    "name": {"type": "string"},
    "description": {"type": "string"},
    "room_id": {
        "type": "integer",
        "minLength": 5,
        "maxLength": 5
    }
}