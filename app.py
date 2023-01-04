import http.client
import sys
from flask import Flask, render_template, request, redirect, url_for
from functions.player_data import * 

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template("main.html")

@app.route('/teams')
def teams():
    return render_template("teams.html")


@app.route('/players', methods = ["POST","GET"])
def players_stats():
    # try:
    if request.method == "POST":
        name = request.form["name"]
        league_name = request.form["league_name"]
        season = request.form["season"]
        country = request.form["country"]
        league_id = get_league_id(league_name,country)
        print(league_id)
        data = player(name,season,league_id)
        print(data)
        return render_template("view_player.html",name=name,data=data,season=season)
    else:
        return render_template("players.html")
# except:
    #     return render_template("error.html")





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)