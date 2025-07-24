from fastapi import APIRouter
from .vacancies import router as vacancies_router
from .registration import router as registration_router
from .login import router as login_router
from .home import router as home_router
from .profile import router as profile_router

from .test import router as test_router

router = APIRouter()

router.include_router(vacancies_router)
router.include_router(login_router)
router.include_router(registration_router)
router.include_router(home_router)
router.include_router(profile_router)

router.include_router(test_router)
