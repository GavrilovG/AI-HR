from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, VARCHAR, DateTime, JSON, ForeignKey
from datetime import datetime

from ..base import Base

from sqlalchemy import ForeignKeyConstraint
from ..models import Vacancy, Candidate

class Interview(Base):
    __tablename__ = "interview"
    __table_args__ = (
        ForeignKeyConstraint(
            columns=["candidate_id"],
            refcolumns=["candidate.id"],
            name="",
            initially="DEFERRED",
        ),
        ForeignKeyConstraint(
            columns=["vacancy_id"],
            refcolumns=["vacancy.id"],
            name="",
            initially="DEFERRED",
        ),
    )
    
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, unique=True)
    candidate_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("user.id"), unique=False)
    vacancy_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("vacancy.id"), unique=False)
    started_at: Mapped[datetime] = mapped_column(DateTime)
    finished_at: Mapped[datetime] = mapped_column(DateTime)
    media_links: Mapped[dict] = mapped_column(JSON)
    
    candidate: Mapped[Candidate] = relationship()
    vacancy: Mapped[Vacancy] = relationship()
