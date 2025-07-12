from fastapi import FastAPI
from .routers import router
from ..db.base import async_connection_db, create_async_engine_db


async def create_app(scope=None):
    app = FastAPI(title="PARAM PAM")
    
    db_session = await async_connection_db(
        engine=await create_async_engine_db()
        )

    
    app.include_router(router)
    @app.get("/")
    async def root():
        return {"message": "OK"}
    
    return app
    