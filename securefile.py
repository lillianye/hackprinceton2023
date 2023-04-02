#!/usr/bin/env python

#-----------------------------------------------------------------------
# securefile.py
# Author: Lillian Ye, Jessica Dong, Michelle Liu
#-----------------------------------------------------------------------

import flask
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import requests

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

@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
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

        url = "https://api.verbwire.com/v1/nft/store/file"

        files = {"filePath": (filepath, open(filepath, "rb"), "image/png")}
        headers = {
            "accept": "application/json",
            "X-API-Key": "sk_live_c07f6ba3-d6fc-4882-a833-51f7f7f6898d"
        }

        response = requests.post(url, files=files, headers=headers)

        print(response.text)
        os.remove(filepath)

        return redirect(url_for('upload', link=response.text[29:-3]))

    if request.method == "GET":
        link = request.args.get("link")
        html_code = flask.render_template('upload.html', link=link)
        response = flask.make_response(html_code)
        return response

if __name__ == '__main__':
    app.run(debug = True)
