import random
from pathlib import Path

from fastapi import APIRouter, HTTPException, Depends
from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.magic_strings import ERRORS
from app.database.database import get_db
from app.logging_config import setup_logging
from app.models.image import Image
from app.schemas.images import RandomImageResponse

router = APIRouter(tags=["images"])

IMAGES_DIR = Path("static/images")

setup_logging()

@logger.catch
@router.get("/random", response_model=RandomImageResponse)
async def get_random_image(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(Image).where(Image.is_active == True))
        images = result.scalars().all()
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=418, detail=ERRORS["something_went_wrong"])

    if not images:
        raise HTTPException(status_code=404, detail=ERRORS["no_images"])
    random_image = random.choice(images)

    return RandomImageResponse(
        filename=random_image.filename,
        file_path=random_image.file_path
    )
