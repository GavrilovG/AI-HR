from pydantic import BaseModel


class UserLoginSchema(BaseModel):
    username: str
    password: str


class VacancyData(BaseModel):
    title: str
    tags: str
    