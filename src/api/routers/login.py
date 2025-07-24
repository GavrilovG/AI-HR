from fastapi import APIRouter
from fastapi import APIRouter, Depends, Response, Request, Form

from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
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
    request: Request,
    response: Response,
    email: str = Form(...),
    password: str = Form(...)
):
    check = await authenticate_user(email=email, password=password)
    if check is None:
        return templates.TemplateResponse("exception.html", {"request": request, "text": "Неверная почта или пароль"})
    access_token = create_access_token({"sub": str(check.id)})
    response = RedirectResponse(url='/profile', status_code=303)
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return response


@router.post("/logout")
async def logout_user():
    response = RedirectResponse(url="/home", status_code=303)
    response.delete_cookie(key="users_access_token")
    return response