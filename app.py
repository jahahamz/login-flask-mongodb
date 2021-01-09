# SETUP
# virtualenv -p python3 env
# source env/bin/activate
# pip install flask pymongo passlib

from flask import Flask, render_template

app = Flask(__name__)

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