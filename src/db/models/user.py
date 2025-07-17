from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, VARCHAR

from ..base import Base

from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum


class UserRole(str, Enum):
    RECRUITER = "recruiter"
    ADMIN = "admin"


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, unique=True
    )

    email: Mapped[str] = mapped_column(VARCHAR(32), nullable=True)
    password: Mapped[str] = mapped_column(VARCHAR(32), nullable=True)
    role: Mapped[UserRole] = mapped_column(SQLAlchemyEnum(UserRole), nullable=False, default=UserRole.RECRUITER)
