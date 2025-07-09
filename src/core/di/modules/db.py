import contextlib
from collections.abc import AsyncIterator, Iterable
from typing import Any

import aioinject
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from ....db.base import async_engine, async_session_factory


@contextlib.asynccontextmanager
async def get_engine() -> AsyncIterator[AsyncEngine]:
    yield async_engine
    await async_engine.dispose()


@contextlib.asynccontextmanager
async def get_session(
    engine: AsyncEngine,
) -> AsyncIterator[AsyncSession]:
    async with async_session_factory.begin() as session:
        yield session


providers: Iterable[aioinject.Provider[Any]] = [
    aioinject.Singleton(get_engine),
    aioinject.Scoped(get_session, type_=AsyncSession),
]
