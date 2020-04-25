create_schema = {
    "first_name": {"type": "string"},
    "last_name": {"type": "string"},
    "email": {"type": "string"},
    "password": {
            "type": "string",
            "minLength": 8,
            "maxLength": 50
    },
}

login_schema = {
    "email": {"type": "string"},
    "password": {
            "type": "string",
            "minLength": 8,
            "maxLength": 50
    },

}