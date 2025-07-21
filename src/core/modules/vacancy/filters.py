from collections.abc import Sequence
from typing import Annotated

from sqla_filter import UNSET, BaseFilter, FilterField, Unset
from sqlalchemy.sql.operators import eq, in_op

from ....db.constants import VacancyStatusEnum
from ....db.models import Vacancy


class VacancyFilterDto(BaseFilter):
    ids: Annotated[
        Sequence[int] | Unset,
        FilterField(Vacancy.id, operator=in_op),
    ] = UNSET
    title: Annotated[
        str | Unset,
        FilterField(Vacancy.title, operator=eq),
    ] = UNSET
    creator_id: Annotated[
        int | Unset,
        FilterField(Vacancy.creator_id, operator=eq),
    ] = UNSET
    status: Annotated[
        Sequence[VacancyStatusEnum] | Unset,
        FilterField(Vacancy.status, operator=in_op),
    ] = UNSET
    
