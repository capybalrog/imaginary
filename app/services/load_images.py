import asyncio
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if root_path not in sys.path:
    sys.path.append(root_path)

from pathlib import Path

from loguru import logger
from sqlalchemy.future import select

from app.database.database import AsyncSessionLocal
from app.logging_config import setup_logging
from app.models.image import Image

setup_logging()


@logger.catch
async def populate_images_from_static(static_path: str = "static/"):
    """
    Сканирует папку static и добавляет изображения в базу данных,
    если они ещё не существуют.
    """
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}
    static_dir = Path(__file__).parent.parent / "static"

    if not static_dir.exists():
        logger.error(f"Папка {static_path} не найдена.")
        return

    async with AsyncSessionLocal() as session:
        for root, _, files in os.walk(static_dir):
            for file in files:
                if Path(file).suffix.lower() in image_extensions:
                    file_path = Path(root) / file
                    relative_path = file_path.relative_to(static_dir)

                    result = await session.execute(
                        select(Image).where(Image.filename == str(relative_path))
                    )
                    existing_image = result.scalars().first()

                    if not existing_image:
                        new_image = Image(
                            filename=str(relative_path),
                            original_filename=file,
                            file_path=str(file_path),
                            storage_type="local",
                        )
                        session.add(new_image)

        await session.commit()
        logger.info("Загрузка изображений завершена.")


def load_images():
    asyncio.run(populate_images_from_static())

if __name__ == "__main__":
    load_images()