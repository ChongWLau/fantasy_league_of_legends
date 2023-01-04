
import json
from behave import then
from behave.api.async_step import async_run_until_complete
from behave.runner import Context
from hamcrest import assert_that, equal_to
from buildpg import render

from fantasy_league_of_legends import models


@then(u'the api-user is returned a list of players')
def the_api_user_is_returned_a_list_of_players(context: Context):
    expected_response = [
        models.BaseLeaguepediaPlayer(**player) for player in context.fake_leaguepedia_response
    ]
    assert_that(json.loads(context.response.text), equal_to(expected_response))


@then(u'the team is saved into the database')
@async_run_until_complete
async def the_team_is_saved_into_the_database(context: Context):
    
    input_data = models.BaseTeam(**context.data)
    
    query = """
        SELECT 
            * 
        FROM
            fantasy_team
    """

    sql, values = render(query)

    async with context.app.state.db_conn.acquire() as conn:
        result = await conn.fetchrow(sql, *values)
    
    db_data = models.BaseTeam(**result)
    print(input_data)
    print(db_data)
    
    assert_that(input_data, equal_to(db_data))