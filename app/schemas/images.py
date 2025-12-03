from pydantic import BaseModel
from pathlib import Path


class RandomImageResponse(BaseModel):
    """Возвращает картинку."""
    filename: str
    file_path: Path

    class Config:
        from_attributes = True
