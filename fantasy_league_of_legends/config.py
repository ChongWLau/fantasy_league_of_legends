import logging
from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PORT: Optional[int] = 8080
    API_HOST: Optional[str] = "0.0.0.0"
    DEBUG: Optional[bool] = False
    LOG_LEVEL_AS_INT: int = logging.INFO
