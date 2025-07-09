from typing import TypeVar
from pydantic_settings import BaseSettings

from pydantic_settings import BaseSettings, SettingsConfigDict

TSettings = TypeVar("TSettings", bound=BaseSettings)


def get_settings(settings):
    print(settings())
    return settings()


class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./.env", env_file_encoding="utf-8", extra="ignore"
    )


class DatabaseSettings(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="db_")

    name: str = "localhost"
    driver: str
    host: str
    port: int = 5432
    user: str
    password: str
    
    echo: bool = True
    
    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
