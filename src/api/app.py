from fastapi import FastAPI
from .routers import router

def create_app(scope=None):
    app = FastAPI(title="PARAM PAM")


    app.include_router(router)
    @app.get("/")
    async def root():
        return {"message": "OK"}
    
    return app
    