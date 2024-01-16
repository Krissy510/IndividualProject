from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

# New decorator for cache
@lru_cache()
def get_settings():
    return Settings()