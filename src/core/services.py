from ..db.models import User
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from ..db.base import async_session, get_session


class UserService:
    def __init__(
        self,
        session = async_session,
    ) -> None:
        self._session = session

    async def get_by_id(self, id):
        print(self._session)
        # return {'a': 'ok'}
        async with self._session() as session:
            user = await session.scalar(statement=select(User).where(User.id == id))
            if user is not None:
                return [user.id, user.username, user.password]
            return "Такого нету"
    
    async def create_user(
        self,
        username,
        password,
    ):
        async with self._session() as session:
            user = User(username=username, password=password)
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return [user.id, user.username, user.password]
