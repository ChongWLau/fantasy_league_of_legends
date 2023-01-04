import uuid
from typing import OrderedDict

from behave import given
from behave.api.async_step import async_run_until_complete
from behave.runner import Context
from buildpg import V, Values
from unittest.mock import AsyncMock, patch

from fantasy_league_of_legends import db


@given("the api-user has a fantasy team")
@async_run_until_complete
async def the_api_user_has_a_fantasy_team(context: Context) -> None:

    # get pool of db connections from the FastAPI application state
    pool = context.app.state.db_conn
    context.fantasy_team_id = uuid.uuid4()

    values = Values(
        id=context.fantasy_team_id, fantasy_name="some team name", fantasy_owner="that guy"
    )

    # render a SQL INSERT string and column values for merging
    sql, values = db.build_insert(
        table=V("fantasy_team"),
        values=values,
    )

    # acquire a db connection and execute the rendered SQL
    # INSERT statement
    async with pool.acquire() as conn:
        _ = await conn.execute(sql, *values)


@given(u'the api is mocked with player data')
@async_run_until_complete
async def the_api_is_mocked_with_player_data(context: Context) -> None:
    context.fake_leaguepedia_response = [
        OrderedDict([('Role', 'Bot'), ('Team', 'Astralis'), ('Player', 'Jeskla')]),
        OrderedDict([('Role', 'Bot'), ('Team', 'Excel Esports'), ('Player', 'Patrik')]),
        OrderedDict([('Role', 'Bot'), ('Team', 'Fnatic'), ('Player', 'Upset')]),
        OrderedDict([('Role', 'Bot'), ('Team', 'G2 Esports'), ('Player', 'Rekkles')]),
        OrderedDict([('Role', 'Bot'), ('Team', 'MAD Lions'), ('Player', 'Carzzy')]),
        OrderedDict([('Role', 'Bot'), ('Team', 'Misfits Gaming'), ('Player', 'Kobbe')]),
        OrderedDict([('Role', 'Bot'), ('Team', 'SK Gaming'), ('Player', 'Jezu')])
    ]
    context.fake_leaguepedia_api = AsyncMock(
        return_value=context.fake_leaguepedia_response
    )
    leaguepedia_patch = patch(
        "fantasy_league_of_legends.leaguepedia.leaguepedia.query",
        context.fake_leaguepedia_api
    )
    leaguepedia_patch.start()
    context.patches.append(leaguepedia_patch)
