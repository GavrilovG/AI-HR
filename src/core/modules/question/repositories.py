
from collections.abc import Sequence
from src.db.models import Question
from sqlalchemy import Select, select
from src.db.base import async_session
from .mapper import mapper

from src.db.models import Question

from .filters import QuestionFilterDto
from .dto import CreateQuestionDto


class QuestionRepository:
    def __init__(
        self,
        session = async_session,
    ) -> None:
        self._session = session

    async def get_question(
        self,
        filter: QuestionFilterDto | None = None
    ) -> Question | None:
        async with self._session() as session:
            question = await session.scalar(self._get_question_stmt(filter))
            return question
    
    async def get_questions(
        self,
        filter: QuestionFilterDto | None = None
    ) -> Sequence[Question]:
        async with self._session() as session:
            questions = await session.scalars(self._get_question_stmt(filter))
            return questions
        
    def _get_question_stmt(
        self,
        filter: QuestionFilterDto | None = None
    ) -> Select[tuple[Question]]:
        stmt = select(Question).order_by(Question.id)
        if filter is not None:
            stmt = filter.apply(stmt)
        return stmt
    
    async def create_question(
        self,
        question: CreateQuestionDto,
    ) -> Question:
        async with self._session() as session:
            question = Question(
                text=question.text,
                order=question.order,
                vacancy_id=question.vacancy_id,
            )
            session.add(question)
            await session.commit()
            await session.refresh(question)
        return question