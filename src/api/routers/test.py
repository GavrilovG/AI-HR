from fastapi import APIRouter

from typing import Annotated
from aioinject import Inject
from aioinject.ext.fastapi import inject
from fastapi import APIRouter, Depends, Request, UploadFile

from ...core.services import UserService

router = APIRouter(prefix='/test_di')

