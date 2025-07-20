from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, VARCHAR
from sqlalchemy import JSON

from ..base import Base
from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum

from ..constants import VacancyStatusEnum


class Vacancy(Base):
    __tablename__ = "vacancy"
    
    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, unique=True
    )
    
    title: Mapped[str] = mapped_column(VARCHAR(32), nullable=True)
    tags: Mapped[str] = mapped_column(VARCHAR(32), nullable=True)
    questions: Mapped[list[dict]] = mapped_column(JSON, nullable=True)
    
    
    # creator_id: Mapped[int] = mapped_column(
    #     BigInteger, foreign_key=True, unique=False
    # )
    
    status: Mapped[VacancyStatusEnum] = mapped_column(
        SQLAlchemyEnum(VacancyStatusEnum),
        default=VacancyStatusEnum.DRAFT,
        nullable=False,
    )
    
    temp_questions: Mapped[list[str]] = mapped_column(JSON, nullable=True)