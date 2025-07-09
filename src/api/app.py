from fastapi import FastAPI
from .routers import router
from ..core.di.container import get_container
from aioinject.ext.fastapi import AioInjectMiddleware


def create_app():
    app = FastAPI(title="PARAM PAM")
    
    app.include_router(router)
    container = get_container()
    app.add_middleware(AioInjectMiddleware, container=container)
    
    @app.get("/")
    async def root():
        return {"message": "OK"}
    
    return app
    