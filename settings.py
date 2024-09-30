from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "DentalStall Scraper"
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0
    redis_password: str = ''

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()