from typing import Literal

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MODE: Literal['DEV', 'TEST', 'PROD']

    USER: str
    PASSWORD: str

    BASE: str
    STANDART: str
    PREMIUM: str
    PROFI: str

    model_config = ConfigDict(env_file=".env")

settings = Settings()