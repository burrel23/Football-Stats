import http.client
import json
import urllib

from flask import Flask, render_template, request
from json2html import json2html

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Bienvenue sur Football Stats"


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
            'x-rapidapi-key': "45489aa3142e552f28903cd2fb5e92de"
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

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')