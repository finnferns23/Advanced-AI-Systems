"""Image helper tools for tarot card assets."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from PIL import Image


def load_card_image(image_path: Path, is_reversed: bool) -> Optional[Image.Image]:
    """Load a card image and rotate it for reversed cards."""
    if not image_path.exists():
        return None
    image = Image.open(image_path)
    if is_reversed:
        return image.rotate(180)
    return image
