from collections.abc import Sequence
from src.core.modules.vacancy.dto import VacancyDto, CreateVacancyDto
from src.core.modules.vacancy.filters import VacancyFilterDto
from .repositories import VacancyRepository
from src.db.constants import VacancyStatusEnum
from .mapper import mapper
from src.db.base import async_session


Repo = VacancyRepository()

async def GetVacancyQuery(
    id: int | None = None,
) -> VacancyDto | None:
    filter = VacancyFilterDto()
    if id is not None:
        filter.ids = [id]
    return mapper(await Repo.get_vacancy(filter))


async def GetVacanciesQuery(
    ids: Sequence[int] | None = None,
    status: VacancyStatusEnum | str | None = None,
) -> Sequence[VacancyDto]:
    filter = VacancyFilterDto()
    if ids is not None:
        filter.ids = ids
    if status is not None:
        filter.status = status.lower()
    return [mapper(vacancy) for vacancy in await Repo.get_vacancys(filter)]


async def CreateVacancyCommand(
    title: str,
    tags: str,
    creator_id: int,
    status: VacancyStatusEnum | str | None = None,
) -> VacancyDto:
    vacancy = CreateVacancyDto(
            title=title,
            tags=tags,
            creator_id=creator_id,
            status=status
        )
    return mapper(await Repo.create_vacancy(vacancy))

async def UpdateVacancyCommand(
    id: int,
    title: str,
    tags: str,
    status: str,
) -> VacancyDto:
    vacancy = await Repo.get_vacancy(VacancyFilterDto(ids=[id]))
    vacancy.title = title
    vacancy.tags = tags
    vacancy.status = status
    async with async_session() as session:
        session.add(vacancy)
        await session.commit()
        await session.refresh(vacancy)
    return mapper(vacancy)
