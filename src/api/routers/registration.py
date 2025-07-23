from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException, Response, Request, Form

from src.api.routers.auth import get_hash
from src.core.modules.user.queries import CreateUserCommand, GetUserQuery

from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="src/api/templates") 

router = APIRouter(prefix='/registration')

@router.get("")
async def register(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})


@router.post("")
async def register(
    request: Request,
    email: str = Form(...),
    full_name: str = Form(...),
    company_name: str = Form(...),
    job_title: str = Form(...),
    password: str = Form(...),
    ):
    user = await GetUserQuery(email=email)
    if user is not None:
        return templates.TemplateResponse("exception.html", {"text": "Email уже зарегистрирован"})
    
    user = await CreateUserCommand(
        email=email,
        full_name=full_name,
        company_name=company_name,
        job_title=job_title,
        password=get_hash(password),
    )
    return {f"создан юзер с параметрами: {str(user)}"}