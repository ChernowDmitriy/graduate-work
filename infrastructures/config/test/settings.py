from pathlib import Path

from dotenv import load_dotenv

from infrastructures.config.base import BaseSettings

load_dotenv(dotenv_path=Path('.env'))


class TestSettings(BaseSettings):
    pass


def get_settings() -> TestSettings:
    return TestSettings(
        _env_file='.env',
        _env_file_encoding='utf-8',
    )
