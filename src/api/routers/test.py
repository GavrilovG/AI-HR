from fastapi import APIRouter

from typing import Annotated, Any, Callable
from aioinject import Inject
from aioinject.ext.fastapi import inject
from fastapi import APIRouter, Depends, Request, UploadFile

from ...core.services import UserService
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)

router = APIRouter(prefix='/test_di')

@router.get('/get_user')
async def blabla(id: int):
    service = UserService()
    return await service.get_by_id(id)

@router.post('/create_user')
async def blabla(username: str, password: str):
    service = UserService()
    return await service.create_user(username, password)