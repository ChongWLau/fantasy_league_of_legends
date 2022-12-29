from fastapi import APIRouter, Request, status
from fantasy_league_of_legends import models
from fantasy_league_of_legends.leaguepedia import get_tournament_players

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
        players = await get_tournament_players()
    except Exception as e:
        logger.warning(
            "There was an error retrieving players from leaguepedia", error=e
        )

    return [models.BaseLeaguepediaPlayer(**player) for player in players]
