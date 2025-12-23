"""Lightweight logging setup for asntools CLIs."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

DEFAULT_LOG_PATH = Path("artifacts") / "asntools.log"


def setup_logging(log_path: Optional[Path | str] = None, level: int = logging.INFO) -> logging.Logger:
    """Configure a shared asntools logger writing to file (and errors to stderr)."""
    target = Path(log_path) if log_path else DEFAULT_LOG_PATH
    target.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("asntools")
    if logger.handlers:
        return logger

    logger.setLevel(level)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s")

    file_handler = logging.FileHandler(target, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stderr_handler = logging.StreamHandler()
    stderr_handler.setLevel(logging.ERROR)
    stderr_handler.setFormatter(formatter)
    logger.addHandler(stderr_handler)

    return logger
