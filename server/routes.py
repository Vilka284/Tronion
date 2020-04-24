from flask import render_template
from server.app import app

@app.route('/')
def index():
    return render_template('landing/index.html')


@app.route('/login')
def login():
    return render_template('login/login.html')


@app.route('/register')
def registration():
    return render_template('registration/registration.html')

''' 
Need to check if user logged in
'''
@app.route('/join')
def join():
    return render_template('join/join.html')


@app.route('/manage')
def manage():
    return render_template('room/manage.html')