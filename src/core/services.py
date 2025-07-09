from ..db.models import User
from sqlalchemy import select
from sqlalchemy.orm import Session


class UserService:
    def __init__(
        self,
        session: Session,
    ) -> None:
        self._session = session

    async def get_by_id(self, id: int):
        user = await self._session.scalar(select(User).where(User.id == id))
        return [user.id, user.username, user.password]
    
    async def create_user(
        self,
        username,
        password,
    ):
        user = User(username=username, password=password)
        self._session.add(user)
        self._session.commit()
        self._session.refresh(user)
        return [user.id, user.username, user.password]
