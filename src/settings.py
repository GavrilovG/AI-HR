from typing import TypeVar
from pydantic_settings import BaseSettings

from pydantic_settings import BaseSettings, SettingsConfigDict

TSettings = TypeVar("TSettings", bound=BaseSettings)


def get_settings(settings):
    return settings()


class DatabaseSettings(BaseSettings):
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
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
    
    @property
    def url_driver(self) -> str:
        return f"{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
