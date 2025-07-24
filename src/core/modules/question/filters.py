from collections.abc import Sequence
from typing import Annotated
from sqla_filter import UNSET, BaseFilter, FilterField, Unset
from sqlalchemy.sql.operators import eq, in_op
from src.db.constants import VacancyStatusEnum
from src.db.models import Question


class QuestionFilterDto(BaseFilter):
    ids: Annotated[
        Sequence[int] | Unset,
        FilterField(Question.id, operator=in_op),
    ] = UNSET
    vacancy_id: Annotated[
        int | Unset,
        FilterField(Question.vacancy_id, operator=eq),
    ] = UNSET
    orders: Annotated[
        Sequence[int] | Unset,
        FilterField(Question.order, operator=in_op),
    ] = UNSET
