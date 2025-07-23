
from sqlalchemy import select
from ....db.base import async_session
from ....db.models import Vacancy




from collections.abc import Sequence
from ....db.models import Vacancy
from sqlalchemy import Select, select
from ....db.base import async_session

from .filters import VacancyFilterDto
from .dto import VacancyDto


class VacancyRepository:
    def __init__(
        self,
        session = async_session,
    ) -> None:
        self._session = session

    async def get_vacancy(
        self,
        filter: VacancyFilterDto | None = None
    ) -> VacancyDto | None:
        async with self._session() as session:
            vacancy = await session.scalar(self._get_vacancy_stmt(filter))
            return VacancyDto(
                        id=vacancy.id,
                        title=vacancy.title,
                        tags=vacancy.tags,
                        creator_id=vacancy.creator_id,
                        status=vacancy.status
                    )
    
    async def get_vacancies(
        self,
        filter: VacancyFilterDto | None = None
    ) -> Sequence[VacancyDto]:
        async with self._session() as session:
            vacancies = await session.scalars(self._get_vacancy_stmt(filter))
            vacancies = [VacancyDto(
                            id=vacancy.id,
                            title=vacancy.title,
                            tags=vacancy.tags,
                            creator_id=vacancy.creator_id,
                            status=vacancy.status
                        ) for vacancy in vacancies]
            return vacancies
        
    def _get_vacancy_stmt(
        self,
        filter: VacancyFilterDto | None = None
    ) -> Select[tuple[Vacancy]]:
        stmt = select(Vacancy).order_by(Vacancy.id)
        if filter is not None:
            stmt = filter.apply(stmt)
        return stmt
