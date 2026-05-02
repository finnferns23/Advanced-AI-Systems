"""Tarot deck loading and validation tools."""

from __future__ import annotations

from pathlib import Path
from typing import Tuple

import pandas as pd

from core.config import DATA_PATH
from core.models import CardMeanings


def load_tarot_data(csv_path: Path = DATA_PATH) -> Tuple[pd.DataFrame, CardMeanings]:
    """Load the original tarot CSV without modifying it."""
    if not csv_path.exists():
        raise FileNotFoundError(f"Tarot data file not found: {csv_path}")

    df = pd.read_csv(csv_path, sep=";", encoding="latin1")
    df.columns = df.columns.str.strip().str.lower()

    required_columns = {"card", "upright", "reversed", "symbolism"}
    missing_columns = sorted(required_columns.difference(df.columns))
    if missing_columns:
        available = ", ".join(df.columns)
        missing = ", ".join(missing_columns)
        raise ValueError(f"Missing CSV columns: {missing}. Available columns: {available}")

    meanings: CardMeanings = {}
    for _, row in df.iterrows():
        card_name = str(row["card"]).strip()
        if not card_name:
            continue
        meanings[card_name] = {
            "upright": str(row["upright"]).strip() if pd.notna(row["upright"]) else "",
            "reversed": str(row["reversed"]).strip() if pd.notna(row["reversed"]) else "",
            "symbolism": str(row["symbolism"]).strip() if pd.notna(row["symbolism"]) else "",
        }

    if not meanings:
        raise ValueError("The tarot CSV was loaded, but no usable card records were found.")

    return df, meanings
