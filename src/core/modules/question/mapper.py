
from src.db.models import Question
from .dto import QuestionDto

def mapper(question: Question | None) -> QuestionDto | None:
    if question is None:
        return None
    return QuestionDto(
        id=question.id,
        text=question.text,
        order=question.order,
        vacancy_id=question.vacancy_id
    )