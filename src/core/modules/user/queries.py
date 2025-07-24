from collections.abc import Sequence
from src.core.modules.user.dto import UserDto, CreateUserDto
from src.core.modules.user.filters import UserFilterDto
from .repositories import UserRepository
from src.db.constants import UserRoleEnum
from .mapper import mapper
from src.db.base import async_session


Repo = UserRepository()

async def GetUserQuery(
    id: int | None = None,
    email: str | None = None,
) -> UserDto | None:
    filter = UserFilterDto()
    if id is not None:
        filter.ids = [id]
    if email is not None:
        filter.email = email
    return mapper(await Repo.get_user(filter))


async def GetUsersQuery(
    ids: Sequence[int] | None = None,
    role: UserRoleEnum | str | None = None,
) -> Sequence[UserDto]:
    filter = UserFilterDto()
    if ids is not None:
        filter.ids = ids
    if role is not None:
        filter.role = role.lower()
    return [mapper(user) for user in await Repo.get_users(filter)]


async def CreateUserCommand(
    email: str,
    full_name: str,
    company_name: str,
    job_title: str,
    password: str,
) -> UserDto:
    user = CreateUserDto(
            email=email,
            full_name=full_name,
            company_name=company_name,
            job_title=job_title,
            password=password,
        )
    return mapper(await Repo.create_user(user))

async def UpdateUserCommand(
    email: str,
    full_name: str,
    company_name: str,
    job_title: str,
) -> UserDto:
    user = await Repo.get_user(UserFilterDto(email=email))
    user.full_name = full_name
    user.company_name = company_name
    user.job_title = job_title
    async with async_session() as session:
        session.add(user)
        await session.commit()
        await session.refresh(user)
    return mapper(user)
