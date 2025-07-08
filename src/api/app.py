from fastapi import FastAPI
from .routers.router import router



def create_app():
    app = FastAPI(title="THE BEST WEB APP MADE BY REMINTA.OFF")
    
    app.include_router(router)
    
    @app.get("/")
    async def root():
        return {"message": "OK"}
    
    return app
    