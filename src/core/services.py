# from ..db.models import User
from sqlalchemy import select
from sqlalchemy.orm import Session

class UserService:
    def __init__(
        self,
        session: Session,
    ) -> None:
        self._session = session

    def get_by_id(self, id: int):
        print(id)
        return f'Такого нету, но все равботает!{id}'
