#!/usr/bin/python3

# Always bring in the Flask class
from flask import Flask

app = Flask(__name__)

# @ is a decorator
# this describes WHEN the code should run
@app.route("/")
def hello_world():
    return "HELLO ZACHS CLASS!!!"

@app.route("/hello/<name>")
def hello_user(name):
    return f"Welcome!!! {name}"


if __name__ == "__main__":
    app.run(port=5006)
