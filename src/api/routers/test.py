from fastapi import APIRouter, Query

from fastapi.templating import Jinja2Templates
from src.core.modules.user.queries import GetUsersQuery


router = APIRouter(prefix='/test')
templates = Jinja2Templates(directory="src/api/templates") 

@router.get('/get_user')
async def blabla():
    user = await GetUsersQuery(role='admin')
    return user
