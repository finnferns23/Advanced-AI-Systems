"""Shared data models and state definitions."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, TypedDict

from core.config import IMAGE_DIR


@dataclass(frozen=True)
class TarotCard:
    """A single drawn tarot card."""

    name: str
    is_reversed: bool = False

    @property
    def orientation(self) -> str:
        """Return the card orientation."""
        return "reversed" if self.is_reversed else "upright"

    @property
    def image_path(self) -> Path:
        """Return the best matching image path while keeping original assets untouched."""
        direct_path = IMAGE_DIR / self.name
        if direct_path.exists():
            return direct_path

        stem_path = Path(self.name)
        if "-" in stem_path.stem:
            prefix, card_slug = stem_path.stem.split("-", 1)
            fallback_path = IMAGE_DIR / f"{prefix}-the{card_slug}{stem_path.suffix}"
            if fallback_path.exists():
                return fallback_path

        return direct_path


@dataclass
class ReadingMemoryItem:
    """One completed reading stored in session memory."""

    question: str
    cards: List[str]
    response: str


@dataclass
class SessionMemory:
    """Simple in-process memory for CLI or non-Streamlit usage."""

    readings: List[ReadingMemoryItem] = field(default_factory=list)

    def add(self, question: str, cards: List[TarotCard], response: str) -> None:
        self.readings.append(
            ReadingMemoryItem(
                question=question,
                cards=[f"{card.name} ({card.orientation})" for card in cards],
                response=response,
            )
        )

    def recent_context(self, limit: int = 3) -> str:
        if not self.readings:
            return "No previous readings in this session."
        recent = self.readings[-limit:]
        lines = []
        for index, item in enumerate(recent, start=1):
            lines.append(f"Previous reading {index}: {item.question} | Cards: {', '.join(item.cards)}")
        return "\n".join(lines)


CardMeanings = Dict[str, Dict[str, str]]


class TarotState(TypedDict, total=False):
    """Shared LangGraph state for the advanced tarot workflow."""

    question: str
    num_cards: int
    cards: List[TarotCard]
    card_details: str
    symbolism: str
    memory_context: str
    draft_response: str
    response: str
    error: str
    validation_notes: str
    model: str
    base_url: str
    session_id: Optional[str]
