from server.app import app

from flask import render_template

@app.route('/')
def index():
    return render_template('landing/index.html')
<<<<<<< HEAD

@app.route('/registration')
def registration():
    return render_template('registration/registration.html')
=======
>>>>>>> 29576f1a80c2f3d328fe8641b6f7278237e9db76
