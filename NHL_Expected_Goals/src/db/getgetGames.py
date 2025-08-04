import requests
import pandas as pd
import sqlite3


url = "https://api-web.nhle.com/v1/club-schedule-season/"
seasonID = "/20242025"

conn = sqlite3.connect('c:\\code\\tw-ds-portfolio\\NHL_Expected_Goals\\src\\db\\nhl.db')
cursor = conn.cursor()

teams = pd.read_sql_query("SELECT teamAbbr FROM teams", conn).teamAbbr

seasonGames = pd.DataFrame(columns = ["gameId",'date', "homeTeam" , "awayTeam"])

test = requests.get("https://api-web.nhle.com/v1/club-schedule-season/TOR/20242025").json()["games"]
print(teams)
for team in teams:
    try:
        season = requests.get(url+team+seasonID).json()["games"]
    except:
        continue
    for game in season:
        if game["homeTeam"]["abbrev"] == team:
            print(game["id"])
            new_row = {"gameId": game["id"],
                        "date": game["gameDate"],
                        "homeTeam" : game["homeTeam"]["id"],
                        "awayTeam" : game["awayTeam"]["id"]
                        }
            seasonGames.loc[len(seasonGames)] = new_row

#Only run once
seasonGames.to_sql("games", conn, if_exists='append',index = False)



gamesTest = pd.read_sql_query("SELECT * FROM games", conn)

print(len(gamesTest))