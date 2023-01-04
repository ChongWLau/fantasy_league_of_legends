from fastapi import APIRouter, Request, status
from fantasy_league_of_legends import models
from fantasy_league_of_legends.leaguepedia import get_tournament_players
from fantasy_league_of_legends.db import create_team

player_router = APIRouter(tags=["player"])
team_router = APIRouter(tags=["team"])


@player_router.get(
    "/players",
    response_model=list[models.BaseLeaguepediaPlayer],
    status_code=status.HTTP_200_OK,
)
async def get_players_api(request: Request) -> list[models.BaseLeaguepediaPlayer]:
    """
    Fetches players from the leaguepedia API
    """
    logger = request.app.state.logger
    try:
        players = get_tournament_players()
    except Exception as e:
        logger.warning(
            "There was an error retrieving players from leaguepedia", error=e
        )

    return [models.BaseLeaguepediaPlayer(**player) for player in players]


@team_router.post(
    "/team",
    response_model=models.ReadTeam,
    status_code=status.HTTP_201_CREATED,
)
async def create_team_api(
    request: Request,
    data: models.BaseTeam
) -> models.ReadTeam:
    """
    Create a team with the data submitted
    """
    db = request.app.state.db_conn
    data_dict = data.dict()

    async with db.acquire() as conn:

        response = await create_team(conn, data_dict)
    
    return response
