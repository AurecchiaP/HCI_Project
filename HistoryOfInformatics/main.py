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
@app.route("/")
def returnMainPage():
    return app.send_static_file("index.html")

@app.route("/home/")
def returnMainPageSecondVersion():
    return app.send_static_file("home.html")

@app.route("/images/<filename>")
def returnImageMain(filename):
    pathToImage=str("static/" + filename)
    return send_file(pathToImage)
    
@app.route("/css/style.css")
def returnCSS():
   return app.send_static_file("style.css")

@app.route("/js/<filename>")
def returnJS(filename):
    pathToJS=str("static/js/" + filename)
    return send_file(pathToJS)


@app.route("/<section>/")
def getIndexPageForSection(section):
    if ("hci" in section):
        return article_generator.hci(section)
    if ("css" in section):
        return app.send_static_file("style.css")
    elif ("ico" in section):
        print("Inside ICO")
        return app.send_static_file("/Logos/favicon.png")
    elif ("the-capsule" in section):
        return app.send_static_file("the-capsule.png")
    elif ("search" in section):
        return app.send_static_file("search.png")
    elif ("arrow" in section):
        return app.send_static_file("arrow.png")
    else:
        return article_generator.create_section(section)
        


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