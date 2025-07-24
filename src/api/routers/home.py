from fastapi import APIRouter, Depends, Query, Request

from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from .auth import get_current_user
from src.core.modules import UserDto
from src.core.modules import GetUsersQuery


router = APIRouter()
templates = Jinja2Templates(directory="src/api/templates") 

@router.get('/home')
async def home(
    request: Request,
    user: UserDto | None = Depends(get_current_user)
):
    if user is None:
        return templates.TemplateResponse("home_unregistered.html", {"request": request})
    return templates.TemplateResponse("home_registered.html", {"request": request})