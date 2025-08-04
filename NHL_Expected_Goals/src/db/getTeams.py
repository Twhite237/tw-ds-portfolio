## Purpose of this script is to query the NHL api for the list of teams

import requests
import pandas as pd
import sqlite3
url = "https://api.nhle.com/stats/rest/en/team"
teams = requests.get(url).json()

teams = teams["data"]
teamsDf = pd.DataFrame.from_dict(teams)
nhlTeamsDf = teamsDf[teamsDf.leagueId == 133]
nhlTeamsDf= nhlTeamsDf.drop(columns=['triCode', 'franchiseId', "leagueId"])
nhlTeamsDf = nhlTeamsDf.rename(columns = {"rawTricode" : "teamAbbr", "id" : "teamId", "fullName" : "teamName"})
print(nhlTeamsDf.head())

conn = sqlite3.connect('c:\\code\\tw-ds-portfolio\\NHL_Expected_Goals\\src\\db\\nhl.db')
cursor = conn.cursor()

res = cursor.execute("SELECT name FROM sqlite_master")
print(res.fetchall())

nhlTeamsDf.to_sql("teams", conn, if_exists='append',index = False)



