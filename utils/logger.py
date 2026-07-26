import logging
from pathlib import Path

log_folder = Path("outputs/logs")
log_folder.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("ResearchSystem")
logger.setLevel(logging.INFO)

if not logger.handlers:

    file_handler = logging.FileHandler(
        log_folder / "app.log",
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)