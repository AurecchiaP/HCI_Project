# -*- coding: utf-8 -*-
from flask import request,make_response,abort
from flask import Flask #Flask is the base server. use 'sudo pip3 install Flask' to install
import os
import common
import dbCreator
# First thing is generate the DB
dbCreator.generateDatabase()

app = Flask(__name__,static_url_path='') 

@app.route("/")
def homePage():
    return app.send_static_file('index.html')

# @app.route("/<section>/<article>")
# def mainPage(section,article):
#     return str(common.getArticleForURL(section, article)["title"])

# Small demo for the current time in unix timestamp
@app.route("/curepochdate")
def curEpochDate():
    return str(common.dateToUnixTimestamp(os.popen("date +\"%Y-%m-%d\"").read()))


if __name__ == "__main__":
    app.debug = True
    
    app.run()