from fastapi import APIRouter
from .vacancies import router as vacancies_router
from .registration import router as registration_router
from .login import router as login_router

from .test import router as test_router

router = APIRouter()

router.include_router(vacancies_router)
router.include_router(login_router)

router.include_router(test_router)
router.include_router(registration_router)


