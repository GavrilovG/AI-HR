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

@router.get('/')
async def blabla():
    service = UserService()
    return await service.get_by_id()
