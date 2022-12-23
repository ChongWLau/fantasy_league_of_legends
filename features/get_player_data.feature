Feature: Fetch player esports data
    
    Scenario: Fetch a list of players from the database
        Given there exists 5 players with the following attributes
        """
        
        """
        When an api-user uses the GET /players endpoint
        Then the player data is saved into the database
