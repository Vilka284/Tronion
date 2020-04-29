from flask import render_template
from server.app import app
from server.auth_jwt import Auth


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
#@Auth.login_required
def join():
    return render_template('join/join.html')


@app.route('/manage')
#@Auth.login_required
def manage():
    return render_template('room/manage.html')


@app.route('/room/<int:id_room>')
def room(id_room):
    return render_template(('room/room.html'))


@app.route('/create_poll')
def create():
    return render_template('room/create_poll.html')


@app.route('/results')
def show_results():
    return render_template('room/results.html')


@app.route('/poll')
def root():
    return render_template('room/poll.html')

