from fastapi import APIRouter
from ...ai.ques_gener import generate_questions_ai
from pydantic import BaseModel
from src.api.shemas import VacancyData



router = APIRouter(prefix='/vacancies')

@router.get('')
async def vacancy():
    '''тут будет отображение списка вакансий'''
    return 'ВАКАНСИЙ НЕТ'


@router.post('')
async def vacancy():
    '''тут будет создание вакансии'''
    return {
        'title': 'да',
        'tags': 'нет'
    }

@router.get('/questions')
async def add_questions(VacancyData: VacancyData):
    return generate_questions_ai(VacancyData.title, VacancyData.tags)


@router.get('/{vacancy_id}')
async def vacancy_detail(vacancy_id: int):
    '''тут будет отображение вакансии по id'''
    return {
        'vacancy_id': vacancy_id,
        'title': 'Example Vacancy',
        'tags': 'example, vacancy'
    }



