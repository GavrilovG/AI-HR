import asyncio
from fastapi import FastAPI
from .routers import router
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)
from ..db.base import async_session
from ..core.services import UserService

def create_app(scope=None):
    app = FastAPI(title="PARAM PAM")


    app.include_router(router)
    @app.get("/")
    async def root():
        return {"message": "OK"}
    
    return app
    