#!/usr/bin/env python

#-----------------------------------------------------------------------
# securefile.py
# Author: Lillian Ye, Jessica Dong, Michelle Liu
#-----------------------------------------------------------------------

import flask
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
app.config['MAX_CONTENT_PATH'] = 16 * 100 * 100

@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    html_code = flask.render_template('index.html')

    response = flask.make_response(html_code)
    return response

@app.route("/user", methods=["GET"])
def user():
    html_code = flask.render_template('user.html')
    response = flask.make_response(html_code)
    return response

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    return redirect(url_for('user'))

@app.route("/send", methods=["POST"])
def send():


if __name__ == '__main__':
    app.run(debug = True)
