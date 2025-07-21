
from collections.abc import Sequence
from ....db.models import User
from sqlalchemy import Select, select
from ....db.base import async_session


from ....db.models import User

from .filters import UserFilterDto
from .dto import UserDto


class UserRepository:
    def __init__(
        self,
        session = async_session,
    ) -> None:
        self._session = session

    async def get_user(
        self,
        filter: UserFilterDto | None = None
    ) -> UserDto | None:
        async with self._session() as session:
            user = await session.scalar(self._get_user_stmt(filter))
            return UserDto(
                id=user.id,
                email=user.email,
                password=user.password,
                role=user.role,
            )
    
    async def get_users(
        self,
        filter: UserFilterDto | None = None
    ) -> Sequence[UserDto]:
        async with self._session() as session:
            users = await session.scalars(self._get_user_stmt(filter))
            users = [UserDto(
                        id=user.id,
                        email=user.email,
                        password=user.password,
                        role=user.role,
                    ) for user in users]
            return users
        
    def _get_user_stmt(
        self,
        filter: UserFilterDto | None = None
    ) -> Select[tuple[User]]:
        stmt = select(User).order_by(User.id)
        if filter is not None:
            stmt = filter.apply(stmt)
        return stmt
