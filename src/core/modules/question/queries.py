from collections.abc import Sequence
from .dto import QuestionDto, CreateQuestionDto
from .filters import QuestionFilterDto
from .repositories import QuestionRepository
from .mapper import mapper
from src.db.base import async_session


Repo = QuestionRepository()

async def GetQuestionQuery(
    id: int | None = None,
    order: int | None = None,
) -> QuestionDto | None:
    filter = QuestionFilterDto()
    if id is not None:
        filter.ids = [id]
    if order is not None:
        filter.orders = [order]
    return mapper(await Repo.get_question(filter))

async def GetQuestionsQuery(
    ids: Sequence[int] | None = None,
    orders: Sequence[int] | None = None,
    vacancy_id: int | None = None,
) -> Sequence[QuestionDto]:
    filter = QuestionFilterDto()
    if ids is not None:
        filter.ids = ids
    if orders is not None:
        filter.orders = orders
    if vacancy_id is not None:
        filter.vacancy_id = vacancy_id
    return [mapper(question) for question in await Repo.get_questions(filter)]


async def CreateQuestionCommand(
    text: str,
    order: int,
    vacancy_id: int
) -> QuestionDto:
    question = CreateQuestionDto(
            text=text,
            order=order,
            vacancy_id=vacancy_id
        )
    return mapper(await Repo.create_question(question))

async def UpdateQuestionCommand(
    id: int,
    text: str,
    order: int,
) -> QuestionDto:
    question = await Repo.get_question(QuestionFilterDto(ids=[id]))
    question.text = text
    question.order = order
    async with async_session() as session:
        session.add(question)
        await session.commit()
        await session.refresh(question)
    return mapper(question)
