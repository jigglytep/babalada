import re
from datetime import datetime
from flask import jsonify
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/test/")
def hello_there():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    # match_object = re.match("[a-zA-Z]+", name)

    clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    dict = {'content': content, 'time': now}
    return jsonify(dict)
