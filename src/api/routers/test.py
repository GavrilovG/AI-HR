from fastapi import APIRouter, Query
from fastapi import APIRouter
from ...core.services import UserRepository, VacancyRepository
from ...core.modules.user.filters import UserFilterDto
from ...core.modules.vacancy.filters import VacancyFilterDto
from ...db.constants import VacancyStatusEnum
from ..schemas import UserLoginSchema

router = APIRouter(prefix='/test')

@router.get('/get_user')
async def blabla(ids: list[int] = Query()):
    service = UserRepository()
    return (await service.get_user(
        UserFilterDto(
            ids=ids,
        )
    ))

@router.get('/get_vacancy')
async def blabla2(status: list[VacancyStatusEnum] = Query()):
    service = VacancyRepository()
    return (await service.get_vacancies(
        VacancyFilterDto(
            status=status
        )
    ))