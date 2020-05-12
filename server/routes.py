from flask import render_template, current_app, url_for
from server.app import app
from server.auth_jwt import Auth

import os


@app.route('/')
def index():
    return render_template('landing/index.html')


@app.route('/login')
def login():
    return render_template('login/login.html')


@app.route('/logout')
def logout():
    return render_template('login/logout.html')


@app.route('/register')
def registration():
    return render_template('registration/registration.html')


@app.route('/join')
# @Auth.login_required
def join():
    return render_template('join/join.html')


@app.route('/manage')
# @Auth.login_required
def manage():
    return render_template('room/manage.html')


@app.route('/room/<int:id_room>')
# @Auth.login_required
def room(id_room=None):
    return render_template(('room/room.html'), id_room=id_room)


@app.route('/manage/<int:id_room>')
# @Auth.login_required
def manage_room(id_room=None):
    return render_template(('room/manage_room.html'), id_room=id_room)


@app.route('/profile')
# @Auth.login_required
def profile():
    return render_template('profile/profile.html')


@app.route('/create_poll')
def create():
    return render_template('polls/create_poll.html')

