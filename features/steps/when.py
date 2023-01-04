import json

from behave import when
from behave.api.async_step import async_run_until_complete
from behave.runner import Context
from httpx import AsyncClient


@when(u'an api-user uses the GET /players endpoint')
@async_run_until_complete
async def an_api_user_uses_the_post_team_endpoint_with_the_following(
    context: Context
) -> None:
    
    async with AsyncClient(app=context.app, base_url="http://testurl") as ac:
        context.response = ac.get(
            "/players"
        )
        context.response.raise_for_status()


@when(u'an api-user uses the POST /team with the following')
@async_run_until_complete
async def an_api_user_uses_the_post_team_with_the_following(context: Context) -> None:
    context.data = json.loads(context.text)

    async with AsyncClient(app=context.app, base_url="http://testurl") as ac:
        response = await ac.post(
            "/team", json=context.data
        )
        response.raise_for_status()
    
    context.response = response
