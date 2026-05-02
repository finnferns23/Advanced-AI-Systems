"""Project configuration for Tarrow Chat Agent."""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "tarots.csv"
IMAGE_DIR = PROJECT_ROOT / "images"
DEFAULT_MODEL = "phi4"
DEFAULT_BASE_URL = "http://localhost:11434"
VALID_SPREADS = (3, 5, 7)
DEFAULT_TEMPERATURE = 0.8
