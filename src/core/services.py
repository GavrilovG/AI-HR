from ..db.models import User
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from ..db.base import async_session, get_session
from ..db.models import Vacancy
from src.ai.ques_gener import generate_questions_ai



class UserService:
    def __init__(
        self,
        session = async_session,
    ) -> None:
        self._session = session

    async def get_by_id(self, id):
        print(self._session)
        # return {'a': 'ok'}
        async with self._session() as session:
            user = await session.scalar(statement=select(User).where(User.id == id))
            if user is not None:
                return [user.id, user.username, user.password]
            return "Такого нету"
    
    async def create_user(
        self,
        username,
        password,
    ):
        async with self._session() as session:
            user = User(username=username, password=password)
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return [user.id, user.username, user.password]


class VacancyService:
    def __init__(
        self,
        session = async_session,
    ) -> None:
        self._session = session
        
        
    async def create_vacancy(
        self,
        title,
        tags,
    ):
        async with self._session() as session:
            vacancy = Vacancy(title=title, tags=tags, questions=[])
            session.add(vacancy)
            await session.commit()
            await session.refresh(vacancy)
            return [vacancy.id, vacancy.title, vacancy.tags]
    
    
    async def add_questions(
        self,
        vacancy_id: int,
        questions: list[str],
    ):
        async with self._session() as session:
            vacancy = await session.scalar(
                select(Vacancy).where(Vacancy.id == vacancy_id)
            )
            if not vacancy:
                return None
            
            vacancy.questions.extend(questions)
            session.add(vacancy)
            await session.commit()
            await session.refresh(vacancy)
            return [vacancy.id, vacancy.title, vacancy.tags, vacancy.questions]
        
        
    async def generate_questions(
    self,
    vacancy_id: int,
    count: int = 5,
    complexity: str = "mid",
):
        async with self._session() as session:
            vacancy = await session.scalar(
                select(Vacancy).where(Vacancy.id == vacancy_id)
            )
            if not vacancy:
                return None

            questions = generate_questions_ai(vacancy.title, vacancy.tags, count=count, complexity=complexity)
            vacancy.questions.extend(questions)
            session.add(vacancy)
            await session.commit()
            await session.refresh(vacancy)
            return [vacancy.id, vacancy.title, vacancy.tags, vacancy.questions]