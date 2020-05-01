import json
from flask import Blueprint, current_app, render_template, url_for, session
from flask_socketio import emit
# from socketio_examples import socketio
from flask_socketio import socketio, emit

room_api = Blueprint('room_api', __name__, static_folder='static',
                     template_folder='templates')


class PollTracker(object):
    """Відслідковуємо загальну кількість голосів для всіх питань"""

    def __init__(self):
        self.polls = {'q1': [0, 0, 0]}
        self.dirty = False

    def add_vote(self, question, answer):
        """Записуємо новий голос"""
        self.polls[question][answer] += 1
        self.dirty = True

    def remove_vote(self, question, answer):
        """Видаляємо голос"""
        self.polls[question][answer] -= 1
        self.dirty = True

    def get_tally(self):
        """Перевірка чи заапдейтились голоса"""
        if self.dirty:
            self.dirty = False
            return self.polls

    def set_dirty(self):
        """Апдейт флаг"""
        self.dirty = True


tally = PollTracker()


@room_api.route('/')
def index():
    #Return the poll administrator client application.
    vote_url = current_app.config.get('POLLS_VOTE_URL') or \
        url_for('room.vote', _external=True)
    return render_template('room/results.html', vote_url=vote_url)


@socketio.on('connect', namespace='/polls')
def on_voter_connect():
    """Нова сесія учасника голосування."""
    # initialize the votes for this participant
    session['votes'] = {}


@socketio.on('disconnect', namespace='/polls')
def on_voter_disconnect():
    """Учасник відконектився"""
    # remove the votes from this participant
    for question, answer in session['votes'].items():
        tally.remove_vote(question, answer)


@socketio.on('vote', namespace='/polls')
def on_voter_vote(question, answer):
    """Новий голос"""
    if question in session['votes']:
        if session['votes'][question] == answer:
            # this is the same vote as before, so it can be ignored
            return
        # remove the previous vote on this question
        tally.remove_vote(question, session['votes'][question])
    # register the new vote
    session['votes'][question] = answer
    tally.add_vote(question, answer)


@socketio.on('votes', namespace='/polls')
def votes(votes):
    """Нові голоса"""
    # remove any previous votes stored in the participant's session
    for question, answer in session['votes'].items():
        tally.remove_vote(question, answer)
    # register the new votes
    for question, answer in votes.items():
        tally.add_vote(question, answer)
    session['votes'] = votes


@socketio.on('connect', namespace='/polls-admin')
def on_admin_connect():
    """Коннект адміна пулу"""
    # send the current tally
    emit('update-charts', tally.polls)


def update_task():
    """Постійне оновлення графіку при нових голосах"""
    while True:
        results = tally.get_tally()
        if results:
            # broadcast the results to all connected admins
            socketio.emit('update-charts', results, namespace='/polls-admin')
        socketio.sleep(5)


socketio.start_background_task(update_task)
