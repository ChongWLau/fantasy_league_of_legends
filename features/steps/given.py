import uuid

from behave import given
from behave.api.async_step import async_run_until_complete
from behave.runner import Context
from buildpg import V, Values

from fantasy_league_of_legends import db


@given("the api-user has a fantasy team")
@async_run_until_complete
async def the_api_user_has_a_fantasy_team(context: Context) -> None:

    # get pool of db connections from the FastAPI application state
    pool = context.app.state.db_conn
    fantasy_team_id = uuid.uuid4()

    values = Values(
        id=fantasy_team_id, fantasy_name="some team name", fantasy_owner="that guy"
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
