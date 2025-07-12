from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, VARCHAR

from .. import Base

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, unique=True
    )

    username: Mapped[str] = mapped_column(VARCHAR(32), nullable=True)
    password: Mapped[str] = mapped_column(VARCHAR(32), nullable=True)
    
