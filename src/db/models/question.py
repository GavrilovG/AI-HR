from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, ForeignKey

from ..base import Base
from sqlalchemy import ForeignKeyConstraint
from ..models import Vacancy

class Question(Base):
    __tablename__ = "question"
    __table_args__ = (
        ForeignKeyConstraint(
            columns=["vacancy_id"],
            refcolumns=["vacancy.id"],
            name="",
            initially="DEFERRED",
        ),
    )
    
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, unique=True)
    text: Mapped[str]
    order: Mapped[int]
    vacancy_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("vacancy.id"), unique=False)

    vacancy: Mapped[Vacancy] = relationship()
