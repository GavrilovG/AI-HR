from aioinject import Scoped, Container, Object, Singleton
from sqlalchemy.orm import Session
from ..db.base import Database, get_session
from ..settings import (
    DatabaseSettings,
    get_settings,
)
from sqlalchemy.ext.asyncio import AsyncSession
from .services import UserService


def create_container() -> Container:
    container = Container()

    for settings_type in [
        DatabaseSettings,
    ]:
        container.register(Object(get_settings(settings_type), settings_type))

    container.register(Singleton(Database))
    container.register(Scoped(get_session, AsyncSession))
    
    
    container.register(Scoped(UserService))
    
    return container
