from flask import Flask, request, make_response,abort

app = Flask(__name__,static_url_path='')

@app.route("/")
def mainPage():
    return app.send_static_file('test.html')

if __name__=="__main__":
    app.debug=True
    app.run()
