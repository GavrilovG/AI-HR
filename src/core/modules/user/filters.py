from collections.abc import Sequence
from typing import Annotated

from sqla_filter import UNSET, BaseFilter, FilterField, Unset
from sqlalchemy.sql.operators import eq, in_op

from src.db.constants import UserRoleEnum
from src.db.models import User


class UserFilterDto(BaseFilter):
    ids: Annotated[
        Sequence[int] | Unset,
        FilterField(User.id, operator=in_op),
    ] = UNSET
    email: Annotated[
        str | Unset,
        FilterField(User.email, operator=eq),
    ] = UNSET
    role: Annotated[
        UserRoleEnum | Unset,
        FilterField(User.role, operator=eq),
    ] = UNSET

