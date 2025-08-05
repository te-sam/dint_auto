from typing import Literal

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MODE: Literal["TEST", "PROD"]

    USER: str
    PASSWORD: str

    BASE: str
    STANDART: str
    PREMIUM: str
    PROFI: str

    EMAIL_ICMP: str
    PASSWORD_ICMP: str

    model_config = ConfigDict(env_file=".env")


settings = Settings()
