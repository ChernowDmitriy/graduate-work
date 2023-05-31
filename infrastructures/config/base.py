import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv(dotenv_path=Path('.env'))


class BaseSettings(BaseModel):
    # Project information
    PROJECT_TITLE: str = os.getenv('PROJECT_TITLE')
    PROJECT_VERSION: str = os.getenv('PROJECT_VERSION')

    # Postgres DB
    POSTGRES_URL: str = os.getenv('POSTGRES_URL')

    # Security
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    HASHING_ALGORITHM: str = os.getenv('HASHING_ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
    REFRESH_TOKEN_EXPIRE_MINUTES: int = int(os.getenv('REFRESH_TOKEN_EXPIRE_MINUTES'))
    JWT_SECRET: str = os.getenv('JWT_SECRET')

    # Validation
    EMAIL_REGEX: str = (
        r"^([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$"
    )
    PASSWORD_MIN_LENGTH: int = 8

    class Config:
        env_file = 'infrastructures/config/.env'
        env_file_encoding = 'utf-8'


def get_settings() -> BaseSettings:
    return BaseSettings()
