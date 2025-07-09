from fastapi import APIRouter

from typing import Annotated
from aioinject import Inject
from aioinject.ext.fastapi import inject
from fastapi import APIRouter, Depends, Request, UploadFile

from ...core.services import UserService

router = APIRouter(prefix='/test_di')


@router.get("")
@inject
async def get_all_words(
    user_sevice: Annotated[UserService, Inject],
):
    return user_sevice.get_by_id(0)
