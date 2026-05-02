"""Prompt and reading formatting tools."""

from __future__ import annotations

from typing import List

from core.models import CardMeanings, TarotCard


def format_card_details(cards: List[TarotCard], meanings: CardMeanings) -> str:
    lines: List[str] = []
    for card in cards:
        card_meaning = meanings.get(card.name, {})
        meaning = card_meaning.get(card.orientation, "Meaning not available.")
        lines.append(f"Card: {card.name}\nOrientation: {card.orientation}\nMeaning: {meaning}")
    return "\n\n".join(lines)


def format_symbolism(cards: List[TarotCard], meanings: CardMeanings) -> str:
    lines: List[str] = []
    for card in cards:
        symbolism = meanings.get(card.name, {}).get("symbolism", "")
        if symbolism:
            lines.append(f"{card.name}: {symbolism}")
    return "\n".join(lines) if lines else "No symbolism data available."


def fallback_reading(question: str, cards: List[TarotCard], meanings: CardMeanings, memory_context: str = "") -> str:
    card_lines = []
    for card in cards:
        meaning = meanings.get(card.name, {}).get(card.orientation, "Meaning not available.")
        card_lines.append(f"- {card.name} ({card.orientation}): {meaning}")

    memory_section = f"\n\nSession memory context:\n{memory_context}" if memory_context else ""
    return (
        "Ollama was not available, so this is a local meaning-based reading.\n\n"
        f"Question or context: {question}{memory_section}\n\n"
        "Cards drawn:\n"
        + "\n".join(card_lines)
        + "\n\nCombined guidance: Look for the shared pattern across these cards. "
        "Treat the reading as a reflective prompt, not a fixed prediction. "
        "The best next step is to choose one practical action you can take today."
    )
