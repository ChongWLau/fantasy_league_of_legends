import asyncio

import structlog
import uvicorn

from fantasy_league_of_legends.app import create_app
from fantasy_league_of_legends.config import Settings

if __name__ == "__main__":
    settings = Settings()
    logger = structlog.get_logger()
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.processors.JSONRenderer(),
            },
        },
        "handlers": {
            "default": {
                "formatter": "json",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr",
            },
            "access": {
                "formatter": "json",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "uvicorn": {
                "handlers": ["default"],
                "level": settings.LOG_LEVEL_AS_INT,
            },
            "uvicorn.error": {
                "level": settings.LOG_LEVEL_AS_INT,
            },
            "uvicorn.access": {
                "handlers": ["access"],
                "level": settings.LOG_LEVEL_AS_INT,
                "propagate": False,
            },
        },
    }

    app = asyncio.run(create_app(logger=logger, settings=settings))
    uvicorn.run(
        app, port=settings.API_PORT, host=settings.API_HOST, log_config=log_config
    )
