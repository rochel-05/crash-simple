import time
from flask import Flask
from flask import render_template, make_response
from flask import flash, Flask, redirect, render_template, request, session, abort, url_for
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from table import *
from test_accuracy_RF import test
import os, subprocess
from werkzeug.utils import secure_filename
from string import Template
from flask_paginate import Pagination, get_page_args
import time

engine = create_engine('sqlite:///usersDb.db', echo=True)
UPLOAD_FOLDER = 'C:/xampp/htdocs/emergencyAlertForACrash/data/'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mkv', 'mpg', 'flv', 'mov', 'wmv', 'webm', '3gp'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/homa/')
def home():
    return render_template('templates/index.php')

@app.route('/homi/')
def home():
    return render_template('/crashsample/templates/index.php')

@app.route('/')
@app.route('/home/', methods=['GET', 'POST'])
def home():
    return render_template('index.php')

@app.route('/login/', methods=['POST'])
def login():
    return home()

@app.route('/logout/')
def logout():
    session['logged_in'] = False
    return home()

@app.route('/detection/')
def detection():
    return render_template('/crashsample/detection.php')

@app.route('/crashDetection/', methods=["GET", "POST"])
def crash_detection():
    return render_template('detection_result.php')

@app.route('/accuracy/')
def accuracy_test():
    return render_template('templates/accuracy.php')

@app.route('/performance/', methods=["GET", "POST"])
def performance():
    return render_template('accuracy.php')

@app.route("/videoBtn/", methods=["GET", "POST"])
def findVideo():
        return render_template('detection.php')

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
        return render_template('detection.php')


@app.route('/video/', methods=['GET', 'POST'])
def videos():
    return render_template('detection.php')

@app.route('/lpr/')
def lpr():
    frame = request.args.get('frame', None)
    return render_template('lpr.php', frame=frame) #, img=img

@app.route('/recognizePlate/', methods=['GET', 'POST'])
def recognizePlate():
    return render_template('lpr.php')

@app.route('/alert/')
def alert():
    return render_template('alert.php')

@app.route('/emergency/', methods=['GET', 'POST'])
def emergency():
    return render_template('alert.php')

@app.route('/urgence/', methods=['GET', 'POST'])
def urgence():
    return render_template('alert.php')

@app.errorhandler(404)
@app.errorhandler(401)
@app.errorhandler(500)
def page_not_found(error):
    return render_template('/crashsample/templates/error.php', code=error.code)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=5000)
