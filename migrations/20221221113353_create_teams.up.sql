CREATE TABLE fantasy_players (
    player_name text PRIMARY KEY,
    player_team text NOT NULL,
    player_role text NOT NULL,
    fantasy_team_id uuid NOT NULL,
    is_playing boolean,
    is_open_for_trade boolean
);
CREATE TABLE fantasy_team (
    id uuid NOT NULL,
    team_name text NOT NULL,
    team_owner text NOT NULL,
    PRIMARY KEY (id)
);
