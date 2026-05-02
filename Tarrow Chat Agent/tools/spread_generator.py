"""Tarot spread generation tools."""

from __future__ import annotations

import random
from typing import List, Optional

from core.config import VALID_SPREADS
from core.models import TarotCard


def draw_cards(num_cards: int, card_names: List[str], seed: Optional[int] = None) -> List[TarotCard]:
    """Draw cards without replacement and assign upright or reversed orientation."""
    if num_cards not in VALID_SPREADS:
        raise ValueError(f"num_cards must be one of {VALID_SPREADS}.")
    if len(card_names) < num_cards:
        raise ValueError("The tarot deck does not contain enough cards for this spread.")

    rng = random.Random(seed)
    selected_cards = rng.sample(card_names, num_cards)
    return [TarotCard(name=card, is_reversed=rng.choice([True, False])) for card in selected_cards]
