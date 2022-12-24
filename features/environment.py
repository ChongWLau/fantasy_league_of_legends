import structlog
from behave.api.async_step import async_run_until_complete
from fantasy_league_of_legends.app import create_app, setup_db_pool
from fantasy_league_of_legends.config import Settings


@async_run_until_complete
async def before_all(context):
    settings = Settings()
    context.logger = structlog.get_logger()
    app = await create_app(context.logger, settings)
    context.settings = settings
    context.app = app


@async_run_until_complete
async def before_scenario(context, scenario):
    context.app.state.db_conn = await setup_db_pool(context.logger, context.settings)

    context.patches = []

    async with context.app.state.db_conn.acquire() as conn:
        async with conn.transaction():
            await conn.execute("DELETE FROM fantasy_team")
            await conn.execute("DELETE FROM fantasy_players")


@async_run_until_complete
async def after_scenario(context, scenario):
    for context_patch in context.patches:
        context_patch.stop()
    await context.app.state.db_conn.close()
