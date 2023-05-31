from pathlib import Path

from dotenv import load_dotenv

from infrastructures.config.base import BaseSettings

load_dotenv(dotenv_path=Path('.env'))


class DevSettings(BaseSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


def get_settings() -> DevSettings:
    return DevSettings()
