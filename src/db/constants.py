from enum import Enum


class VacancyStatusEnum(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"


class UserRoleEnum(str, Enum):
    RECRUITER = "recruiter"
    ADMIN = "admin"

