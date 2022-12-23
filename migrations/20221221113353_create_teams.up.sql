CREATE TABLE player_pool (
    player VARCHAR PRIMARY KEY,
    team VARCHAR NOT NULL,
    player_role VARCHAR NOT NULL,
    fantasy_team_id UUID
);
CREATE TABLE fantasy_team (
    id UUID PRIMARY KEY,
    team_name VARCHAR NOT NULL,
    team_owner VARCHAR NOT NULL
);
-- CREATE TABLE fantasy_members (
--     player VARCHAR NOT NULL,
--     fantasy_team_id UUID,
-- );