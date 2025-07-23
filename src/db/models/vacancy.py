from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, VARCHAR, DateTime
from datetime import datetime

from ..base import Base
from sqlalchemy import Enum as SQLAlchemyEnum

from ..constants import VacancyStatusEnum

from sqlalchemy import ForeignKeyConstraint
from ..models import User


class Vacancy(Base):
    __tablename__ = "vacancy"
    __table_args__ = (
        ForeignKeyConstraint(
            columns=["creator_id"],
            refcolumns=["user.id"],
            name="",
            initially="DEFERRED",
        ),
    )
    
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, unique=True)
    title: Mapped[str]
    tags: Mapped[str]
    creator_id: Mapped[int] = mapped_column(BigInteger, foreign_key=True, unique=False)
    status: Mapped[VacancyStatusEnum] = mapped_column(SQLAlchemyEnum(VacancyStatusEnum), default=VacancyStatusEnum.DRAFT, nullable=False,)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    
    creator: Mapped[User] = relationship()
