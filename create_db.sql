DROP DATABASE tronion IF EXISTS;
CREATE DATABASE tronion ENCODING ‘UTF8’;
\connect tronion


CREATE TABLE account ( id_user SERIAL PRIMARY KEY , first_name VARCHAR(20) NOT NULL, last_name VARCHAR(20) NOT NULL, email VARCHAR(35) NOT NULL, password VARCHAR(35) NOT NULL
);

CREATE TABLE room ( id_room SERIAL PRIMARY KEY, name_room VARCHAR(20) NOT NULL, note VARCHAR(1000)
);

CREATE TABLE poll ( id_poll SERIAL PRIMARY KEY, question VARCHAR(30) NOT NULL, life_time TIME, room_id INTEGER, FOREIGN KEY (room_id) REFERENCES room(id_room) ON DELETE CASCADE
);

CREATE TABLE message ( id_message SERIAL PRIMARY KEY, content VARCHAR(1000), date_send TIMESTAMP, room_id INTEGER, user_id INTEGER, FOREIGN KEY (room_id) REFERENCES room(id_room) ON DELETE CASCADE, FOREIGN KEY (user_id) REFERENCES account(id_user) ON DELETE CASCADE
);

CREATE TABLE answer ( id_answer SERIAL PRIMARY KEY, note VARCHAR(50), poll_id INTEGER, FOREIGN KEY (poll_id) REFERENCES poll(id_poll) ON DELETE CASCADE
);

CREATE TABLE answer_has_user ( user_id INTEGER, answer_id INTEGER, FOREIGN KEY (user_id) REFERENCES account(id_user) ON DELETE CASCADE, FOREIGN KEY (answer_id) REFERENCES answer(id_answer) ON DELETE CASCADE
);

CREATE TABLE room_has_user ( user_id INTEGER, room_id INTEGER, FOREIGN KEY (user_id) REFERENCES account(id_user) ON DELETE CASCADE, FOREIGN KEY (room_id) REFERENCES room(id_room) ON DELETE CASCADE
);
