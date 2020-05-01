from flask import render_template, current_app, url_for
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


@app.route('/vote')
@Auth.login_required
def vote():
    """Return the poll participant client application."""
    return render_template('room/vote.html')


@app.route('/join')
@Auth.login_required
def join():
    return render_template('join/join.html')


@app.route('/manage')
@Auth.login_required
def manage():
    return render_template('room/manage.html')


@app.route('/room/<int:id_room>')
@Auth.login_required
def room(id_room=None):
    return render_template(('room/room.html'), id_room=id_room)


@app.route('/profile')
@Auth.login_required
def profile():
    return render_template('profile/profile.html')


@app.route('/create_poll')
def create():
    return render_template('room/create_poll.html')


@app.route('/polls')
def show_results():

    # Return the poll administrator client application.
    vote_url = current_app.config.get('POLLS_VOTE_URL') or \
        url_for('vote', _external=True)

    return render_template('room/results.html', vote_url=vote_url)



