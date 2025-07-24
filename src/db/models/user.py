from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, VARCHAR, DateTime

from ..base import Base
from sqlalchemy import Enum as SQLAlchemyEnum
from ..constants import UserRoleEnum
from datetime import datetime

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, unique=True)
    full_name: Mapped[str]
    email: Mapped[str] = mapped_column(VARCHAR(32), unique=True, nullable=False)
    password: Mapped[str]  = mapped_column(VARCHAR(32), nullable=False)
    company_name: Mapped[str]
    job_title: Mapped[str]
    role: Mapped[UserRoleEnum] = mapped_column(SQLAlchemyEnum(UserRoleEnum), nullable=False, default=UserRoleEnum.RECRUITER)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())
