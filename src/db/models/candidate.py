from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger

from ..base import Base

class Candidate(Base):
    __tablename__ = "candidate"
    
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, unique=True)
    full_name: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
