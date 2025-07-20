from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, VARCHAR

from ..base import Base
from sqlalchemy import Enum as SQLAlchemyEnum
from ..constants import UserRoleEnum

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, unique=True
    )

    email: Mapped[str] = mapped_column(VARCHAR(32), nullable=True)
    password: Mapped[str] = mapped_column(VARCHAR(32), nullable=True)
    role: Mapped[UserRoleEnum] = mapped_column(SQLAlchemyEnum(UserRoleEnum), nullable=False, default=UserRoleEnum.RECRUITER)
