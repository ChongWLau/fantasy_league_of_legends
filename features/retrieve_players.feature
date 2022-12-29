Feature: Retrieving players from leaguepedia

    Scenario: Retrieve a list of players
        Given the api is mocked with player data
        When an api-user uses the GET /players endpoint
        Then the api-user is returned a list of players
    
    # Scenario: Retrieve a list of players with filters
    #     Given the api is mocked with player data
    #     When an api-user uses the GET /players with the following