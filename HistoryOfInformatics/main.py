# -*- coding: utf-8 -*-
from flask import request,make_response,abort
from flask import Flask #Flask is the base server. use 'sudo pip3 install Flask' to install
import os
import common



app = Flask(__name__,static_url_path='') 

@app.route("/")
def mainPage():
    return "Hello World"

# Small demo for the current time in unix timestamp
@app.route("/curepochdate")
def curEpochDate():
    return str(common.dateToUnixTimestamp(os.popen("date +\"%Y-%m-%d\"").read()))


if __name__ == "__main__":
    app.debug = True
    app.run()