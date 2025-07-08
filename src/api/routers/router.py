from fastapi import APIRouter, Depends, HTTPException, Response
from authx import AuthX, AuthXConfig
from pydantic import BaseModel


openai_api_key = 'sk-SwDj282n2Anwwu96iaisTDxPUf1n15hG'



router = APIRouter()
config = AuthXConfig()
config.JWT_SECRET_KEY = "your_secret_key"
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)

class UserLoginSchema(BaseModel):
    username: str
    password: str

@router.get("/hello")
async def hello():
    return {"message": "HELLO MY DEAR FRIEND!!!"}


@router.post("/login")
async def login(creds: UserLoginSchema, response: Response):
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


class VacancyData(BaseModel):
    title: str
    tags: str
    


@router.post('/vacancies')
async def vacancy(vac_data: VacancyData):
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


def generate_questions_ai(title: str, tags: str):
    import openai
    prompt = (f"Ты — опытный hr-специалист. Сейчас ты составляешь вопросы для собеседования на вакансию '{title}'. "
        f"Кандидат должен обладать навыками: {tags}. Сгенерируй ровно 15 вопросов. "
        "Вопросы должны быть релевантны вакансии и направлены на оценку как профессиональных навыков, так и soft skills. Выведи просто список из вопросов без пояснений или дополнительных комментариев."
        )
    
    client = openai.OpenAI(
    api_key=openai_api_key,
    base_url="https://api.proxyapi.ru/openai/v1"
    )
    messages=[
                {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=1000,
        temperature=0.7
    )
    
    ans = response.choices[0].message.content
    return {
        'title': title,
        'tags': tags,
        'questions': ans
    }


@router.post('/vacancies/questions')
async def add_questions(vac_data: VacancyData):
    return generate_questions_ai(vac_data.title, vac_data.tags)

