from dataclasses import dataclass

from src.db.constants import VacancyStatusEnum
from datetime import datetime
from ..user.dto import UserDto

@dataclass
class VacancyDto:
    id: int
    title: str
    tags: str
    creator_id: int
    status: str
    created_at: datetime
    
@dataclass
class CreateVacancyDto:
    title: str
    tags: str
    creator_id: int
    status: str
