
import requests
import pandas as pd
import sqlite3

url = "https://api-web.nhle.com/v1/gamecenter/"
ext = "/play-by-play"

conn = sqlite3.connect('c:\\code\\tw-ds-portfolio\\NHL_Expected_Goals\\src\\db\\nhl.db')
cursor = conn.cursor()

gameIds = pd.read_sql_query("SELECT gameId FROM games", conn).gameId


shotsDf = pd.DataFrame(columns = ["eventId", "gameId", "teamId", "xDistance", "yDistance", "zoneCode", "homeTeamDefendingSide", "result"])
for game in gameIds:
    print(url+str(game)+ext)
    try:
        gameId = requests.get(url+str(game)+ext).json()["id"]
        gamePlays = requests.get(url+str(game)+ext).json()["plays"]
    except:
        continue

    for play in gamePlays:
        print(play["eventId"])
        if (play["typeDescKey"] == "goal" or 
            play["typeDescKey"] == "shot-on-goal" or 
            play["typeDescKey"] == "blocked-shot" or
            play["typeDescKey"] == "blocked-shot"):

            try:
                new_row = {"gameId": gameId,
                            "eventId": play["eventId"],
                            "teamId" : play["details"]["eventOwnerTeamId"],
                            "xDistance" : play["details"]["xCoord"],
                            "yDistance" : play["details"]["yCoord"],
                            "zoneCode" : play["details"]["zoneCode"],
                            "homeTeamDefendingSide" : play["homeTeamDefendingSide"],
                            "result" : play["typeDescKey"]
                            }
                shotsDf.loc[len(shotsDf)] = new_row

            except:
                continue

print(shotsDf.head())



shotsDf.to_sql("shots", conn, if_exists='append',index = False)

playsTest = pd.read_sql_query("SELECT * FROM plays LIMIT 5", conn)

print(playsTest.head())
            
            

