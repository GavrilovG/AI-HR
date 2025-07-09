from fastapi import APIRouter, Depends, HTTPException, Response
from authx import AuthX, AuthXConfig
from pydantic import BaseModel
from src.api import shemas
from src.api.ai.ques_gener import generate_questions_ai




router = APIRouter()
config = AuthXConfig()
config.JWT_SECRET_KEY = "your_secret_key"
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)



@router.get("/hello")
async def hello():
    return {"message": "HELLO MY DEAR FRIEND!!!"}


@router.post("/login")
async def login(creds: shemas.UserLoginSchema, response: Response):
    if creds.username == "admin" and creds.password == "password":
        authx = AuthX(config)
        access_token = authx.create_access_token(uid='12345') # , identity=creds.username
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, access_token)
        return {"access_token": access_token}
    raise HTTPException(status_code=401, detail="Invalid credentials")


@router.get("/setting", dependencies=[Depends(security.access_token_required)])
async def setting():
    return {"message": "You are authenticated as HR and can set interview parameters."}


@router.get("/vacancies")
async def vacancy():
    '''тут будет отображение списка вакансий'''
    return 'ВАКАНСИЙ НЕТ'



@router.post('/vacancies')
async def vacancy(vac_data: shemas.VacancyData):
    '''тут будет создание вакансии'''
    return {
        'title': vac_data.title,
        'tags': vac_data.tags
    }
    
    
@router.get('/vacancies/{vacancy_id}')
async def vacancy_detail(vacancy_id: int):
    '''тут будет отображение вакансии по id'''
    return {
        'vacancy_id': vacancy_id,
        'title': 'Example Vacancy',
        'tags': 'example, vacancy'
    }




@router.post('/vacancies/questions')
async def add_questions(vac_data: shemas.VacancyData):
    return generate_questions_ai(vac_data.title, vac_data.tags)

