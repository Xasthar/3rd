import os
from flask import Flask, render_template

app = Flask(__name__)

# routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
def home():
    return render_template('dashboard.html')