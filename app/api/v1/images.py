from pathlib import Path

from fastapi import APIRouter

router = APIRouter(tags=["images"])

IMAGES_DIR = Path("static/images")
