# SETUP
# virtualenv -p python3 env
# source env/bin/activate
# pip install flask pymongo passlib

from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
app.debug = True

# Databaseç
client = MongoClient('localhost', 27017)
db = client.user_login_system

# Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')
# Run --> ./run
# sudo chmod +x run
# ./run