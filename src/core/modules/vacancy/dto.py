from dataclasses import dataclass

from src.db.constants import VacancyStatusEnum
from datetime import datetime

@dataclass(slots=True, frozen=True, kw_only=True)
class VacancyDto:
    id: int
    title: str
    tags: str
    creator_id: int
    status: VacancyStatusEnum
    created_at: datetime
