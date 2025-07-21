from dataclasses import dataclass

from ....db.constants import UserRoleEnum


@dataclass(slots=True, frozen=True, kw_only=True)
class UserDto:
    id: int
    email: str
    password: str
    role: UserRoleEnum
