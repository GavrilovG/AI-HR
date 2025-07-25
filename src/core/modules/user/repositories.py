
from collections.abc import Sequence
from src.db.models import User
from sqlalchemy import Select, select
from src.db.base import async_session
from .mapper import mapper

from src.db.models import User

from .filters import UserFilterDto
from .dto import CreateUserDto


class UserRepository:
    def __init__(
        self,
        session = async_session,
    ) -> None:
        self._session = session

    async def get_user(
        self,
        filter: UserFilterDto | None = None
    ) -> User | None:
        async with self._session() as session:
            user = await session.scalar(self._get_user_stmt(filter))
            return user
    
    async def get_users(
        self,
        filter: UserFilterDto | None = None
    ) -> Sequence[User]:
        async with self._session() as session:
            users = await session.scalars(self._get_user_stmt(filter))
            return users
        
    def _get_user_stmt(
        self,
        filter: UserFilterDto | None = None
    ) -> Select[tuple[User]]:
        stmt = select(User).order_by(User.id)
        if filter is not None:
            stmt = filter.apply(stmt)
        return stmt
    
    async def create_user(
        self,
        user: CreateUserDto,
    ) -> User:
        async with self._session() as session:
            user = User(
                full_name=user.full_name,
                email=user.email,
                password=user.password,
                company_name=user.company_name,
                job_title=user.job_title,
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user