from fastapi import APIRouter
from fastapi import APIRouter, Depends, Response, Request, Form

from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from src.core.modules import UserDto
from .auth import authenticate_user, create_access_token, get_current_user
from src.core.modules import UpdateUserCommand


router = APIRouter(prefix='/profile')
templates = Jinja2Templates(directory="src/api/templates") 



@router.post("/update")
async def update_profile(
    request: Request,
    user: UserDto | None = Depends(get_current_user),
    full_name: str = Form(...),
    job_title: str = Form(...),
    company_name: str = Form(...)
):
    # Здесь должна быть логика обновления данных пользователя
    user = await UpdateUserCommand(
        email=user.email,
        full_name=full_name,
        company_name=company_name,
        job_title=job_title
    )
    
    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
            "user": user,
            "message": "Данные успешно обновлены!"
        }
    )
    
@router.get("/")
async def get_me(
    request: Request,
    user: UserDto | None = Depends(get_current_user)
):
    if user is None:
        return RedirectResponse(url="/login", status_code=307)
    return templates.TemplateResponse(
        "profile.html",
        {"request": request,
         "user": user,}
    )