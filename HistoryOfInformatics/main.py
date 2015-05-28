# -*- coding: utf-8 -*-
from flask import request,make_response,abort,send_file
from flask import Flask #Flask is the base server. use 'sudo pip3 install Flask' to install
import os
import common
import dbCreator
import article_generator
# First thing is generate the DB
dbCreator.generateDatabase()

app = Flask(__name__,static_url_path='') 

@app.route("/<section>/<article>")
def mainPage(section,article):
    return article_generator.create_article(section,article)
    
@app.route("/<section>/images/<filename>")
def returnImage(section,filename):
    pathToImage=str("static/images/" + filename)
    return send_file(pathToImage)

# Small demo for the current time in unix timestamp
@app.route("/curepochdate")
def curEpochDate():
    return str(common.dateToUnixTimestamp(os.popen("date +\"%Y-%m-%d\"").read()))


if __name__ == "__main__":
    app.debug = True
    
    app.run()