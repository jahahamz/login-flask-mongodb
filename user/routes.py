from flask import Flask
from app import app
from user.models import User

@app.route('/user/signup/', methods=['POST'])
def signup():
    return User().signup()

@app.route('/user/logout/')
def signout():
    return User().logout()