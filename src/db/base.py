from ..settings import DatabaseSettings
from collections.abc import AsyncGenerator, Generator
from contextlib import contextmanager

from sqlalchemy import orm, MetaData
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)

Base = declarative_base()

class Database:
    def __init__(self, settings: DatabaseSettings) -> None:
        self._engine = create_async_engine(
            settings.url_driver,
            echo=settings.echo,
        )
        self.session_factory = orm.scoped_session(
            async_sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )


# async def create_async_engine_db(
#     config: DbConfig,
#     echo: bool,
# ) -> AsyncEngine:
#     return create_async_engine(config.conn(), echo=echo)


# async def async_connection_db(
#     engine: AsyncEngine,
#     expire_on_commit: bool,
# ) -> AsyncSession:
#     return async_sessionmaker(engine, expire_on_commit=expire_on_commit)

@contextmanager
async def get_session(database: Database) -> AsyncGenerator[AsyncSession]:
    with database.session_factory.begin() as session:
        yield session
