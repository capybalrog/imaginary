from contextlib import asynccontextmanager

import fastapi_swagger_dark as fsd
from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.v1 import images
from app.core.magic_strings import BASE_TEXTS
from app.services.load_images import load_images

app = FastAPI(
    title=BASE_TEXTS["app_title"],
    version=BASE_TEXTS["app_version"],
    description=BASE_TEXTS["app_description"],
    docs_url=None,
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(images.router, prefix="/api/v1/images", tags=["images"])

# Тёмная тема для свагера
swagger_router = APIRouter()
fsd.install(swagger_router, path="/swagger")
app.include_router(swagger_router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    load_images()
    yield


@app.get("/")
async def root():
    return {
        "version": BASE_TEXTS["app_version"],
        "title": BASE_TEXTS["app_title"],
        "description": BASE_TEXTS["app_description"],
        "message": BASE_TEXTS["root_message"],
        "author": BASE_TEXTS["author"],
    }
