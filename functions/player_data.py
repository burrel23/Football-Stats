import http.client
import json
from flask import request

def get_league_id(league_name,country):
    
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    if len(league_name.split()) > 1 : 
        league_name = league_name.split()[0]+"%20"+league_name.split()[1]

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "45489aa3142e552f28903cd2fb5e92de"
        }
    conn.request("GET", "/leagues?name="+league_name+"&country="+country, headers=headers)
    # conn.request("GET", "/leagues?name=ligue%201&country=france", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    info = json.loads(data)
    id = info["response"][0]["league"]["id"]
    print(info["response"][0]["league"]["id"])
    return id




def player(name,season,league_id):
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")
    league_id = str(league_id)

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "45489aa3142e552f28903cd2fb5e92de"
        }

    # conn.request("GET", "/players?search=Neymar&season=2019&league=61", headers=headers)
    conn.request("GET", "/players?search="+name+"&season="+season+"&league="+league_id, headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    info = json.loads(data)
    print(info)
    return info["response"][0]
    print(info["response"][0])


