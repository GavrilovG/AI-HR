from dataclasses import dataclass

from ....db.constants import VacancyStatusEnum


@dataclass(slots=True, frozen=True, kw_only=True)
class VacancyDto:
    id: int
    title: str
    tags: str
    creator_id: int
    status: VacancyStatusEnum
