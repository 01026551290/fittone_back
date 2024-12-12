# app/core/config.py

from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()