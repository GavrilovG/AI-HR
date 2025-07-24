
from collections.abc import Sequence
from src.db.models import Vacancy
from sqlalchemy import Select, select
from src.db.base import async_session
from .mapper import mapper

from src.db.models import Vacancy

from .filters import VacancyFilterDto
from .dto import CreateVacancyDto


class VacancyRepository:
    def __init__(
        self,
        session = async_session,
    ) -> None:
        self._session = session

    async def get_vacancy(
        self,
        filter: VacancyFilterDto | None = None
    ) -> Vacancy | None:
        async with self._session() as session:
            vacancy = await session.scalar(self._get_vacancy_stmt(filter))
            return vacancy
    
    async def get_vacancys(
        self,
        filter: VacancyFilterDto | None = None
    ) -> Sequence[Vacancy]:
        async with self._session() as session:
            vacancys = await session.scalars(self._get_vacancy_stmt(filter))
            return vacancys
        
    def _get_vacancy_stmt(
        self,
        filter: VacancyFilterDto | None = None
    ) -> Select[tuple[Vacancy]]:
        stmt = select(Vacancy).order_by(Vacancy.id)
        if filter is not None:
            stmt = filter.apply(stmt)
        return stmt
    
    async def create_vacancy(
        self,
        vacancy: CreateVacancyDto,
    ) -> Vacancy:
        async with self._session() as session:
            vacancy = Vacancy(
                title=vacancy.title,
                tags=vacancy.tags,
                creator_id=vacancy.creator_id,
                status=vacancy.status
            )
            session.add(vacancy)
            await session.commit()
            await session.refresh(vacancy)
            return vacancy