import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/login")
def login_page():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
