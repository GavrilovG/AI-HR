from dataclasses import dataclass


@dataclass
class QuestionDto:
    id: int
    text: str
    order: int
    vacancy_id: int

@dataclass
class CreateQuestionDto:
    text: str
    order: int
    vacancy_id: int
