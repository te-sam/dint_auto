from loguru import logger
import sys

logger.add(
    sink=sys.stdout,  # Стандартный вывод с цветами
    level="DEBUG",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>",
)
