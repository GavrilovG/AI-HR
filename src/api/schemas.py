from pydantic import BaseModel
from typing import Literal, List, Optional

class UserLoginSchema(BaseModel):
    username: str
    password: str

    
class VacancyCreate(BaseModel):
    title: str
    tags: str
    

class VacancyDB(BaseModel):
    id: str
    title: str
    tags: str
    
    
class Question(BaseModel):
    question: str


class GenerateQuestionsRequest(BaseModel):
    count: int = 5
    complexity: Literal["easy", "mid", "hard"] = "mid"
    

class AddGeneratedQuestionsRequest(BaseModel):
    questions: List[Question]