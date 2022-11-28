import uuid
from fastapi import FastAPI
from structlog import BoundLogger
from fantasy_league_of_legends.config import Settings


async def create_app(logger: BoundLogger, settings: Settings):
    app = FastAPI()
    app.state.id = str(uuid.uuid4())
    app.state.settings = settings
    app.state.logger = logger
    
    @app.on_event("startup")
    async def startup():
        logger.info("Startup Complete!")
    
    @app.on_event("shutdown")
    async def shutdown():
        logger.info("Shutdown Complete!")
    
    # app.include_router(team_router)
    logger.info("App Created!")
    
    return app
