from fastapi import FastAPI, Request
from .routers import router

def create_app(scope=None):
    app = FastAPI(title="PARAM PAM")


    app.include_router(router)
    
    return app
    