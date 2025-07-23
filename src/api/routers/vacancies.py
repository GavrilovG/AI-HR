from fastapi import APIRouter, Depends, status, Request, Response
from ...ai.ques_gener import generate_questions_ai
from ...core.services import VacancyRepository
from src.api import schemas
# from src.api.routers.login import auth

router = APIRouter(prefix='/api/vacancies')



@router.post('')
async def vacancy(
    vacancy_data: schemas.VacancyCreate,
    # current_user: dict = Depends(auth.access_token_required)
):
    service = VacancyRepository()
    return await service.create_vacancy(title=vacancy_data.title, tags=vacancy_data.tags)


@router.post("/{vacancy_id}/questions")
async def add_question(
    vacancy_id: int,
    question: schemas.Question,
    # current_user: dict = Depends(auth.access_token_required)
):
    service = VacancyRepository()
    return await service.add_questions(vacancy_id=vacancy_id, questions=[question.question])


@router.post('{vacancy_id}/generate-questions')
async def generate_questions(
    vacancy_id: int,
    gen_params: schemas.GenerateQuestionsRequest,
    # current_user: dict = Depends(auth.access_token_required)
):
    service = VacancyRepository()
    return await service.generate_questions(vacancy_id=vacancy_id)


@router.post("/{vacancy_id}/add-generated-questions")
async def add_generated_questions(
    vacancy_id: int,
    add_request: schemas.AddGeneratedQuestionsRequest,
    # current_user: dict = Depends(auth.access_token_required)
):
    service = VacancyRepository()
    return await service.generate_questions(vacancy_id=vacancy_id, questions=add_request.questions)


@router.delete("/{vacancy_id}/questions/{question_id}")
async def delete_question(
    vacancy_id: int,
    question_id: int,
    # current_user: dict = Depends(auth.access_token_required)
):
    service = VacancyRepository()
    return await service.delete_question(vacancy_id=vacancy_id, question_id=question_id)


@router.post("/{vacancy_id}/publish")
async def publish_vacancy(
    vacancy_id: int,
    # current_user: dict = Depends(auth.access_token_required)
):
    service = VacancyRepository()
    return await service.publish_vacancy(vacancy_id=vacancy_id)


@router.get("/{vacancy_id}")
async def get_vacancy(
    vacancy_id: int,
    # current_user: dict = Depends(auth.access_token_required)
):
    service = VacancyRepository()
    return service.get_vacancy(vacancy_id=vacancy_id)