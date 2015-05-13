# -*- coding: utf-8 -*-
from flask import request,make_response,abort
from flask import Flask #Flask is the base server. use 'sudo pip3 install Flask' to install
import os
app = Flask(__name__,static_url_path='') 

@app.route("/")
def mainPage():
    return "Hello World"
    
import jinja2 #Used to substitute the tags in the html

def jinjaSubstitution(dictWithValues,jinjaFilename):
    templateLoader = jinja2.FileSystemLoader( searchpath="/" )
    #Get the current path of this file. From here, put togehter the path of the template file
    basePath = os.path.dirname(os.path.abspath(__file__))
    # An environment provides the data necessary to read and
    #   parse our templates.  We pass in the loader object here.
    templateEnv = jinja2.Environment( loader=templateLoader )

    # This constant string specifies the template file we will use.
    #TEMPLATE_FILE = basePath + "/JinjaTemplates/table.jinja"
    TEMPLATE_FILE = basePath + "/Templates/" + jinjaFilename
    # Read the template file using the environment object.
    # This also constructs our Template object.
    template = templateEnv.get_template( TEMPLATE_FILE )

    # Specify any input variables to the template as a dictionary.
    templateVars = dictWithValues

    # Finally, process the template to produce our final text.
    outputText = template.render( templateVars )

    return outputText



if __name__ == "__main__":
    app.debug = True
    app.run()