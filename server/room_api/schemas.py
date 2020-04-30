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

poll_create_schema = {
    "question": {"type": "string"},
    "life_time": {"type": "string"},
    "note": {"type": "string"}
}