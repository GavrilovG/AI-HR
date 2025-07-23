from dataclasses import dataclass

from ....db.constants import UserRoleEnum
from datetime import datetime

@dataclass
class UserDto:
    id: int
    full_name: str
    email: str
    password: str
    company_name: str
    job_title: str
    role: UserRoleEnum
    created_at: datetime

@dataclass
class CreateUserDto:
    full_name: str
    email: str
    password: str
    company_name: str
    job_title: str