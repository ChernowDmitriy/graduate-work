import os
from pathlib import Path

from dotenv import load_dotenv

from infrastructures.config.base import BaseSettings

load_dotenv(dotenv_path=Path('.env'))


class TestSettings(BaseSettings):
    SYNC_POSTGRES_URL: str = os.getenv('SYNC_POSTGRES_URL', os.getenv('SYNC_POSTGRES_URL').replace('+asyncpg', ''))


def get_settings() -> TestSettings:
    return TestSettings(
        _env_file='.env',
        _env_file_encoding='utf-8',
    )
