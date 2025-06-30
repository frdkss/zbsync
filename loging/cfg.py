from pathlib import Path
from loguru import logger
import sys

LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "app.log"

logger.remove()

logger.add(
    str(LOG_FILE),
    level="INFO",
    rotation="5 MB",
    retention=1,
    format="{file}:{line} | {function}() | {time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    enqueue=True,
)

# В консоль: INFO+ короткий формат
logger.add(
    sys.stdout,
    level="INFO",
    format="{time:HH:mm:ss} | {level} | {message}",
    enqueue=True,
)
