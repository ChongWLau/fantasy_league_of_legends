# Feature: Update their fantasy team
# @wip
#     Scenario: Add a player to their fantasy team
#         Given the api-user has a fantasy team
#         When an api-user uses the POST /team/{team_name} endpoint with the following
#         """
#         {
        
#         }
#         """
#         Then the player data is saved into the database
#         And the api-user is the owner of that player added

#     Scenario: Retrieve members of their team
#         Given the api-user has a fantasy team
#         And their team contains the following players
#         """
#         {

#         }
#         """
#         When the api-user uses the GET /team/{team_name} endpoint
#         Then the players of their team are returned
    
#     Scenario: Remove a player from their fantasy team
#         Given the api-user has a fantasy team
#         And their team contains the following players
#         """
#         {

#         }
#         """
#         When the api-user uses the DELETE /team/{team_name}/{player} endpoint
#         Then the player is removed from their team