import os

from dotenv import load_dotenv

from app.core.magic_strings import BASE_TEXTS

load_dotenv()


class Settings:
    PROJECT_NAME: str = BASE_TEXTS["app_title"]
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")
    DATABASE_URL: str = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    class Config:
        env_file = ".env"


settings = Settings()
