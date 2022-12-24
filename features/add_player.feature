Feature: Add a player to fantasy team
    
    Scenario: Fetch a list of players from the database
        Given the api-user has a fantasy team
        And the api is mocked with player data
        When an api-user uses the POST /fantasy endpoint with the following
        """
        
        """
        Then the player data is saved into the database
        And the api-user is the owner of that player added
