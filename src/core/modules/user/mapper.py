
from src.db.models import User
from .dto import UserDto

def mapper(user: User | None) -> UserDto | None:
    if user is None:
        return None
    return UserDto(
        id=user.id,
        full_name=user.full_name,
        email=user.email,
        password=user.password,
        company_name=user.company_name,
        job_title=user.job_title,
        role=user.role,
        created_at=user.created_at
    )