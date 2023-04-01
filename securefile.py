#!/usr/bin/env python

#-----------------------------------------------------------------------
# securefile.py
# Author: Lillian Ye, Jessica Dong, Michelle Liu
#-----------------------------------------------------------------------

import flask

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
	html_code = flask.render_template('index.html')

	response = flask.make_response(html_code)
	return response

@app.route("/user", methods=["GET"])
def user():
	file_path_param = 'test'
	html_code = flask.render_template('user.html', file_name_param=file_path_param)

	response = flask.make_response(html_code)
	return response
