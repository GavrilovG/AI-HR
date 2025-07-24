from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from .routers import router

def create_app(scope=None):
    app = FastAPI(title="PARAM PAM")


    app.include_router(router)

    return app
    