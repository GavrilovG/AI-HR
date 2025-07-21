from enum import Enum


class VacancyStatusEnum(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    CLOSED = "closed"


class UserRoleEnum(str, Enum):
    RECRUITER = "recruiter"
    ADMIN = "admin"

