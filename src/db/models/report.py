from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import JSON, BigInteger, ForeignKey

from ..base import Base

from sqlalchemy import ForeignKeyConstraint
from ..models import Interview

class Report(Base):
    __tablename__ = "report"
    __table_args__ = (
        ForeignKeyConstraint(
            columns=["interview_id"],
            refcolumns=["interview.id"],
            name="",
            initially="DEFERRED",
        ),
    )
    
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, unique=True)
    interview_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("interview.id"), unique=True)
    transcript: Mapped[dict] = mapped_column(JSON)
    cheating_attempts: Mapped[dict] = mapped_column(JSON)
    scores: Mapped[dict] = mapped_column(JSON)
    
    interview: Mapped[Interview] = relationship()
