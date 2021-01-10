# SETUP
# virtualenv -p python3 env
# source env/bin/activate
# pip install flask pymongo passlib

from flask import Flask, render_template, session, redirect
from pymongo import MongoClient
from functools import wraps

app = Flask(__name__)
#app.debug = True

# Secret key to use 'session', generate using python -c 'import os; print(os.urandom(16))'
app.secret_key = "b'\xbd\x86\t\xa3_\xd4\xbc;t\xb0\xbfp\xb3^#4'"

# Database
client = MongoClient('localhost', 27017)
db = client.user_login_system

# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*arg, **kwargs):
        if 'logged_in' in session:
            return f(*arg, **kwargs)
        else:
            return redirect('/')
    return wrap

def already_logged_in(f):
    @wraps(f)
    def wrap(*arg, **kwargs):
        if 'logged_in' in session:
            return redirect('/dashboard/')
        else:
            return f(*arg, **kwargs)
    return wrap    

# Routes
from user import routes

@app.route('/')
@already_logged_in
def home():
    return render_template('home.html')

@app.route('/register/')
def register():
    return render_template('register.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')


# Run --> ./run
# sudo chmod +x run
# ./run