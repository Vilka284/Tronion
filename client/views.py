from server.app import app

from flask import render_template

'''
Тут пишуться всі views, можна буде додати ще admin_views
'''
@app.route('/')
def index():
    return render_template('landing/index.html')
