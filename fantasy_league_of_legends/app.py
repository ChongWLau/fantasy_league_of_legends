import asyncio
import uuid

import asyncpg
from fastapi import FastAPI
from structlog import BoundLogger

from fantasy_league_of_legends.config import Settings
from fantasy_league_of_legends.api import player_router


async def setup_db_pool(logger, settings: Settings) -> asyncpg.Pool | None:
    logger.info("starting database pool")
    attempts = 0
    connected = False
    while not connected:
        logger.info(f"DB connection attempt: #{attempts}")
        try:
            pool = await asyncpg.create_pool(
                host=settings.DB_HOST,
                user=settings.DB_USER,
                password=settings.DB_PASS,
                database=settings.DB_NAME,
                port=settings.DB_PORT,
            )
            connected = True
            return pool
        except Exception as e:
            if attempts >= settings.MAX_DB_ATTEMPTS:
                raise
            attempts += 1
            logger.error("error starting connection pool", exc_info=e)
            await asyncio.sleep(1)
    return None


async def create_app(logger: BoundLogger, settings: Settings):
    app = FastAPI()
    app.state.id = str(uuid.uuid4())
    app.state.settings = settings
    app.state.logger = logger

    @app.on_event("startup")
    async def startup():
        logger.info("Creating DB Pool...")
        app.state.db_conn = await setup_db_pool(app.state.logger, app.state.settings)
        logger.info("DB Pool Created!")
        logger.info("Startup Complete!")

    @app.on_event("shutdown")
    async def shutdown():
        logger.info("Shutdown Complete!")

    app.include_router(player_router)
    logger.info("App Created!")

    return app
