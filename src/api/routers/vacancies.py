from fastapi import APIRouter, Depends, status, Request, Response
from ...ai.ques_gener import generate_questions_ai
from ...core.services import VacancyService
from src.api import schemas
from login import security

router = APIRouter(prefix='/api/vacancies')



@router.post('',
             status_code=status.HTTP_201_CREATED,
             dependencies=security.access_token_required)
async def vacancy(
    vacancy_data: schemas.VacancyCreate,
    current_user: dict = Depends(security.get_current_user)
):
    service = VacancyService()
    return await service.create_vacancy(title=vacancy_data.title, tags=vacancy_data.tags)


@router.post("/{vacancy_id}/questions",
             dependencies=security.access_token_required)
async def add_question(
    vacancy_id: str,
    question: schemas.Question,
    current_user: dict = Depends(security.get_current_user)
):
    service = VacancyService()
    return await service.add_questions(vacancy_id=vacancy_id, questions=[question.question])


@router.post('{vacancy_id}/generate-questions',
             dependencies=security.access_token_required)
async def generate_questions(
    vacancy_id: str,
    gen_params: schemas.GenerateQuestionsRequest,
    current_user: dict = Depends(security.get_current_user)
):
    service = VacancyService()
    return await service.generate_questions(vacancy_id=vacancy_id)



    
    return await service.add_questions(
        vacancy_id=vacancy_id, questions=questions)




