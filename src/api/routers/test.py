from fastapi import APIRouter, Query
from fastapi import APIRouter
from ...core.services import UserRepository
from ...core.modules.user.filters import UserFilterDto
from ..schemas import UserLoginSchema

router = APIRouter(prefix='/test')

@router.get('/get_user')
async def blabla(ids: list[int] = Query()):
    service = UserRepository()
    return (await service.get_users(
        UserFilterDto(
            ids=ids,
        )
    ))

@router.post('/create')
async def blabla2(user: UserLoginSchema):
    service = UserRepository()
    return await service.create_user(username, password)