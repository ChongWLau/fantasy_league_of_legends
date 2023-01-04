Feature: Creating a fantasy team

    Scenario: Create their fantasy team
        When an api-user uses the POST /team with the following
        """
        {
            "team_name": "A-Team",
            "team_owner": "Mr T"
        }
        """
        Then the team is saved into the database
