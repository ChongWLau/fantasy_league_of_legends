import logging
from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PORT: Optional[int] = 8080
    API_HOST: Optional[str] = "0.0.0.0"
    DEBUG: Optional[bool] = False
    LOG_LEVEL_AS_INT: int = logging.INFO
    DB_HOST: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_PORT: int
    MAX_DB_ATTEMPTS: int = 10
