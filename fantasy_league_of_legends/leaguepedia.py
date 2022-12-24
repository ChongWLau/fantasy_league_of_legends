from leaguepedia_parser.site.leaguepedia import leaguepedia

# def get_tournament_teams(tournament: str)

x = leaguepedia.query(
    tables="Tournaments",
    fields=", ".join({"Name", "OverviewPage", "League"}),
    where=f"Tournaments.League ='LoL EMEA Championship'",
    # where=f"Tournaments.OverviewPage ='LEC/2021 Season/Summer Season'",
)

y = leaguepedia.query(
    tables="Leagues",
    fields=", ".join({"League", "Region", "League_Short"}),
    where=f"Leagues.Region ='Europe'",
)

z = leaguepedia.query(
    tables="TournamentRosters",
    fields=", ".join({"Team"}),
    where=f"TournamentRosters.OverviewPage ='LEC/2021 Season/Summer Season'",
)

a = leaguepedia.query(
    tables="TournamentPlayers",
    fields=", ".join({"Team", "Player", "Role"}),
    where=f"TournamentPlayers.OverviewPage ='LEC/2021 Season/Summer Season'",
)

print(a)

# for team in z:
#     print(team['Team'])