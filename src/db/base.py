import logging

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)

from ..settings import DatabaseSettings, get_settings

Base = declarative_base()


async def create_async_engine_db(
    echo: True,
) -> AsyncEngine:
    return create_async_engine(get_settings(DatabaseSettings).url, echo=echo)


async def async_connection_db(
    engine: AsyncEngine,
    expire_on_commit: bool = True,
) -> AsyncSession:
    return async_sessionmaker(engine, expire_on_commit=expire_on_commit)