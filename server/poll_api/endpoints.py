import json
from flask import Blueprint, current_app, render_template, url_for, session
from flask_socketio import emit
from server.app import sio, db

poll_api = Blueprint('poll_api', __name__)


class PollTracker(object):
    """Відслідковуємо загальну кількість голосів для всіх питань"""

    def __init__(self):
        self.polls = {'q1': [0, 0, 0]}
        self.dirty = False

    def add_vote(self, question, answer):
        """Записуємо новий голос"""
        # print("add_vote")
        self.polls[question][answer] += 1
        self.dirty = True

    def remove_vote(self, question, answer):
        # print("remove_vote")
        """Видаляємо голос"""
        self.polls[question][answer] -= 1
        self.dirty = True

    def get_tally(self):
        # print("get_tally")
        """Перевірка чи заапдейтились голоса"""
        if self.dirty:
            self.dirty = False
            return self.polls

    def set_dirty(self):
        # print("set_dirty")
        """Апдейт флаг"""
        self.dirty = True


tally = PollTracker()


@poll_api.route('/')
def show_results():
    # print("show_results")
    """Return the poll administrator client application."""
    vote_url = current_app.config.get('POLLS_VOTE_URL') or \
        url_for('poll_api.vote', _external=True)
    return render_template('polls/results.html', vote_url=vote_url)


@poll_api.route('/vote')
def vote():
    # print("vote")
    """Return the poll participant client application."""
    return render_template('polls/vote.html')


@sio.on('connect', namespace='/polls')
def on_voter_connect():
    # print("on_voter_connect")
    """Нова сесія учасника голосування."""
    # initialize the votes for this participant
    session['votes'] = {}


@sio.on('disconnect', namespace='/polls')
def on_voter_disconnect():
    """Учасник відконектився"""
    # print("on_voter_disconnect")
    # remove the votes from this participant
    for question, answer in session['votes'].items():
        tally.remove_vote(question, answer)


@sio.on('vote', namespace='/polls')
def on_voter_vote(question, answer):
    """Новий голос"""
    # print("on_voter_vote")
    if question in session['votes']:
        if session['votes'][question] == answer:
            # this is the same vote as before, so it can be ignored
            return
        # remove the previous vote on this question
        tally.remove_vote(question, session['votes'][question])
    # register the new vote
    session['votes'][question] = answer
    tally.add_vote(question, answer)


@sio.on('votes', namespace='/polls')
def votes(votes):
    # print("votes")
    """Нові голоса"""
    # remove any previous votes stored in the participant's session
    for question, answer in session['votes'].items():
        tally.remove_vote(question, answer)
    # register the new votes
    for question, answer in votes.items():
        tally.add_vote(question, answer)
    session['votes'] = votes


@sio.on('connect', namespace='/polls-admin')
def on_admin_connect():
    # print("on_admin_connect")
    """Коннект адміна пулу"""
    # send the current tally
    sio.emit('update-charts', tally.polls)


def update_task():
    # print("update_task")
    """Постійне оновлення графіку, коли нові голоса"""
    while True:
        results = tally.get_tally()
        # results = tally.set_dirty()

        if results:
            # broadcast the results to all connected admins
            sio.emit('update-charts', results, namespace='/polls-admin')
        sio.sleep(3)


sio.start_background_task(update_task)
