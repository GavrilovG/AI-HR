from fastapi import APIRouter, Depends, Form, HTTPException, status, Request, Response
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from src.ai.ques_gener import generate_questions_ai
from .auth import get_current_user
from src.core.modules import UserDto, GetVacancyQuery, GetUserQuery, UpdateVacancyCommand

router = APIRouter(prefix='')
templates = Jinja2Templates(directory="src/api/templates") 

@router.get("/vacancy/{id}")
async def get_vacancy(
    request: Request,
    id: int,
    user: UserDto | None = Depends(get_current_user),
):
    vacancy = await GetVacancyQuery(id=id)
    creator = await GetUserQuery(id=vacancy.creator_id)
    print(vacancy, creator)
    if vacancy is None:
        return HTTPException(status_code=404)
    if vacancy.creator_id != user.id and user.role != "ADMIN":
        return HTTPException(status_code=403)
    return templates.TemplateResponse("vacancy.html", {"request": request, "vacancy": vacancy, "creator": creator})

@router.post("/vacancy/{id}/update")
async def get_vacancy(
    request: Request,
    id: int,
    user: UserDto | None = Depends(get_current_user),
    title: str = Form(...),
    tags: str = Form(...),
    status: str = Form(...)
):
    vacancy = await GetVacancyQuery(id=id)
    if vacancy.creator_id != user.id and user.role != "ADMIN":
        return RedirectResponse(url='/profile', status_code=303)
    vacancy = await UpdateVacancyCommand(id=id, title=title, tags=tags, status=status)
    return RedirectResponse(url=f"/vacancy/{id}", status_code=303)
    