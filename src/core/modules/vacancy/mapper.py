
from src.db.models import Vacancy
from .dto import VacancyDto
from ..user.mapper import mapper as user_mapper

def mapper(vacancy: Vacancy | None) -> VacancyDto | None:
    if vacancy is None:
        return None
    return VacancyDto(
        id=vacancy.id,
        title=vacancy.title,
        tags=vacancy.tags,
        creator_id=vacancy.creator_id,
        status=vacancy.status.name,
        created_at=vacancy.created_at,
    )