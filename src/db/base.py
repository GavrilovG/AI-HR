import logging
from typing import AsyncGenerator

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

engine = create_async_engine(get_settings(DatabaseSettings).url, echo=True)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=True
)

async def get_session():
    async with async_session() as session:
        yield session