import sqlite3
con = sqlite3.connect('c:\\code\\tw-ds-portfolio\\NHL_Expected_Goals\\src\\db\\nhl.db')

cur = con.cursor()


#cur.execute("CREATE TABLE players(playerId, playerName, teamId)")
#cur.execute("CREATE TABLE teams(teamName, teamId, teamAbbr)")
#cur.execute("CREATE TABLE games(gameId, date, homeTeam, awayTeam)")
cur.execute("CREATE TABLE shots(eventId, gameId, teamId, xDistance, yDistance, zoneCode, homeTeamDefendingSide, result )")


#res = cur.execute("SELECT name FROM sqlite_master")
#print(res.fetchall())


#cur.execute("DROP TABLE shots")

## Tables
#Teams

#Players

#Play by play (shots and goals only)
#types of shots: "shot-on-goal", "blocked-shot","missed-shot", "goal"
# Other columns : eventOwnerTeamId




