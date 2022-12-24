CREATE TABLE fantasy_players (
    player_name VARCHAR PRIMARY KEY,
    player_team VARCHAR NOT NULL,
    player_role VARCHAR NOT NULL,
    fantasy_team_id UUID NOT NULL
);
CREATE TABLE fantasy_team (
    id UUID PRIMARY KEY,
    fantasy_name VARCHAR NOT NULL,
    fantasy_owner VARCHAR NOT NULL
);
