from fastapi import HTTPException
from src.db.constants import VacancyStatusEnum
from ....db.models import User
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from ....db.base import async_session, get_session
from ....db.models import Vacancy
from src.ai.ques_gener import generate_questions_ai
import uuid


class VacancyRepository:
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
            vacancy = Vacancy(title=title, tags=tags, questions=[], status=VacancyStatusEnum.DRAFT)
            session.add(vacancy)
            await session.commit()
            await session.refresh(vacancy)
            return [vacancy.id, vacancy.title, vacancy.tags]
    
    
    async def get_vacancy(
        self,
        vacancy_id: int,
    ):
        async with self._session() as session:
            vacancy = await session.scalar(
                select(Vacancy).where(Vacancy.id == vacancy_id)
            )
            if not vacancy:
                raise HTTPException(404, "Vacancy not found")
            return [vacancy.id, vacancy.title, vacancy.tags, vacancy.questions, vacancy.status]
    
    
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
            vacancy.temp_questions.extend(questions)
            session.add(vacancy)
            await session.commit()
            await session.refresh(vacancy)
            return [vacancy.id, vacancy.title, vacancy.tags, vacancy.questions]
        
        
        async def add_generated_questions(
            self,
            vacancy_id: int,
            questions: list[str],
        ):
            async with self._session() as session:
                vacancy = await session.scalar(
                    select(Vacancy).where(Vacancy.id == vacancy_id)
                )
                if not vacancy:
                    raise HTTPException(404, "Vacancy not found")
                
                for question in questions:
                    question_id = str(uuid.uuid4())
                    new_question = {
                        "id": question_id,
                        "question": question
                    }
                    vacancy.questions.append(new_question)
                session.add(vacancy)
                await session.commit()
                await session.refresh(vacancy)
                return [vacancy.id, vacancy.title, vacancy.tags, vacancy.questions]
            
        
    async def delete_question(
        self,
        vacancy_id: int,
        question_id: int,
    ):
        async with self._session() as session:
            vacancy = await session.scalar(
                select(Vacancy).where(Vacancy.id == vacancy_id)
            )
            vacancy.questions = [
                question for question in vacancy.questions if question["id"] != question_id
            ]
            session.add(vacancy)
            await session.commit()
            await session.refresh(vacancy)
            return [vacancy.id, vacancy.title, vacancy.tags, vacancy.questions]
        
    
    async def publish_vacancy(
        self,
        vacancy_id: int,
    ):
        async with self._session() as session:
            vacancy = await session.scalar(
                select(Vacancy).where(Vacancy.id == vacancy_id)
            )
            if not vacancy:
                raise HTTPException(404, "Vacancy not found")   
            vacancy.status = VacancyStatusEnum.PUBLISHED
            session.add(vacancy)
            await session.commit()
            await session.refresh(vacancy)
            return [vacancy.id, vacancy.title, vacancy.tags, vacancy.status]