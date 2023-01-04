import http.client
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template("main.html")


@app.route('/teams')
def teams():
    return render_template("teams.html")