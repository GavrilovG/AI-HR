from fastapi import APIRouter
from fastapi import APIRouter, Depends, Response, Request, Form

from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from src.core.modules.user.dto import UserDto
from .auth import authenticate_user, create_access_token, get_current_user


router = APIRouter(prefix='')
templates = Jinja2Templates(directory="src/api/templates") 


@router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login(
    response: Response,
    email: str = Form(...),
    password: str = Form(...)
):
    check = await authenticate_user(email=email, password=password)
    if check is None:
        return templates.TemplateResponse("exception.html", {"text": "Неверная почта или пароль"})
    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}

@router.get("/me")
async def get_me(user: UserDto = Depends(get_current_user)):
    return user

@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {'message': 'Пользователь успешно вышел из системы'}