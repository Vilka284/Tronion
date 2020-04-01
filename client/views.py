from server.app import app

from flask import render_template

@app.route('/')
def index():
    return render_template('landing/index.html')

@app.route('/join')
def join():
    return render_template('join/join.html')

@app.route('/registration')
def registration():
    return render_template('registration/registration.html')

