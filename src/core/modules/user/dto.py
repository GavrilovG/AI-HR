from dataclasses import dataclass

from src.db.constants import UserRoleEnum
from datetime import datetime

@dataclass
class UserDto:
    id: int
    full_name: str
    email: str
    password: str
    company_name: str
    job_title: str
    role: str
    created_at: datetime

@dataclass
class CreateUserDto:
    full_name: str
    email: str
    password: str
    company_name: str
    job_title: str