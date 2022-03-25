from sportsipy.nfl.teams import Teams
from sportsipy.nfl.roster import Roster

for team in Teams():
    print(team)
    rost = Roster(team.abbreviation, '2020')
    print(rost.coach)
    for player in rost.players:
        print(player.name)
    # break