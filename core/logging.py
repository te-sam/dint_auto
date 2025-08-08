import sys

from loguru import logger

from core.config import settings


logger.add(
    sink=sys.stdout,  # Стандартный вывод с цветами
    level=settings.LOGGING_LEVEL,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>",
)

__all__ = ["logger"]