from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class BaseTeam(BaseModel):
    team_owner: str
    team_name: str


class UpdateTeam(BaseModel):
    team_name: str


class ReadTeam(BaseTeam):
    """
    Response model for all Team related endpoints
    """
    id: UUID


class BaseLeaguepediaPlayer(BaseModel):
    Player: str
    Team: str
    Role: str


class BasePlayer(BaseModel):
    player_name: str
    player_team: str
    player_role: str


class UpdatePlayer(BasePlayer):
    fantasy_team_id: Optional[UUID]
    is_playing: Optional[bool] = False
    is_open_for_trade: Optional[bool] = False


class ListFantasyTeam(UpdateTeam):
    players: list[BasePlayer]
    benched: list[BasePlayer]


class ListLeaguepediaPlayers(BaseModel):
    players: list[BasePlayer]
