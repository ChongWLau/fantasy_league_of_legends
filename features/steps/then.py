
import json
from behave import then
from behave.api.async_step import async_run_until_complete
from behave.runner import Context
from hamcrest import assert_that, equal_to

from fantasy_league_of_legends import models


@then(u'the api-user is returned a list of players')
def the_api_user_is_returned_a_list_of_players(context: Context):
    expected_response = [
        models.BaseLeaguepediaPlayer(**player) for player in context.fake_leaguepedia_response
    ]
    assert_that(json.loads(context.response.text), equal_to(expected_response))
