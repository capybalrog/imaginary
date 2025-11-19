from sqlalchemy import JSON, Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import Boolean

from app.database.database import Base


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False, unique=True)
    original_filename = Column(String(255), nullable=False)
    file_path = Column(String(500))  # Путь к файлу, если храним локально
    file_size = Column(Integer)  # Размер в байтах
    mime_type = Column(String(100))  # image/jpeg, image/png и т.д.
    title = Column(String(255))
    description = Column(Text)
    tags = Column(JSON)  # Список тегов
    width = Column(Integer)
    height = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)

    # Для облачного хранения
    storage_type = Column(String(50), default="local")  # local, s3, gcs
    storage_path = Column(String(500))  # Путь в облачном хранилище
