import http.client
import json
import sys
import urllib
from flask import Flask, render_template, request, redirect, url_for
from json2html import json2html
from functions.player_data import * 
from dotenv import load_dotenv
import os

app = Flask(__name__)



@app.route('/')
def welcome():
    return render_template("main.html")


@app.route('/teams')
def teams():
    return render_template("teams.html")


@app.route('/team_stats', methods=['GET', 'POST'])
def team_stats():
    try:
        team_name = urllib.parse.quote_plus(request.args['team_name'])
        league_name = urllib.parse.quote_plus(request.args['league_name'])
        season = request.args['season'].strip()

        conn = http.client.HTTPSConnection("v3.football.api-sports.io")

        headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': api_key()
        }

        conn.request("GET", "/teams?name=" + team_name, headers=headers)

        res = conn.getresponse()
        data = res.read()

        team_id = json.loads(data)["response"][0]["team"]["id"]

        conn.request("GET", "/leagues?name=" + league_name, headers=headers)

        res = conn.getresponse()
        data = res.read()

        league_id = json.loads(data)["response"][0]["league"]["id"]

        conn.request("GET",
                        "/teams/statistics?league=" + str(league_id) + "&season=" + season + "&team=" + str(team_id),
                        headers=headers)

        res = conn.getresponse()
        data = res.read()

        stats = json.loads(data)["response"]

        return json2html.convert(json=stats)
    except:
        return render_template("error.html")


@app.route('/players', methods = ["POST","GET"])
def players_stats():
    try:
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
    except:
        return render_template("error.html")





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)