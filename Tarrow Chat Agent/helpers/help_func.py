"""Backward-compatible helper functions for older imports."""

from __future__ import annotations

from types import SimpleNamespace
from typing import Any, Iterable

from agents.interpretation_agent import build_llm
from core.config import DEFAULT_BASE_URL, DEFAULT_MODEL
from tools.reading_formatter import format_card_details, format_symbolism
from tools.spread_generator import draw_cards


def generate_random_draw(num_cards: int, card_names_dataset: Iterable[str]) -> list[dict[str, Any]]:
    """Return drawn cards in the original dictionary format used by the first app."""
    return [
        {"name": card.name, **({"is_reversed": True} if card.is_reversed else {})}
        for card in draw_cards(num_cards, list(card_names_dataset))
    ]


def _card_like(item: dict[str, Any]) -> SimpleNamespace:
    is_reversed = bool(item.get("is_reversed", False))
    return SimpleNamespace(
        name=item["name"],
        is_reversed=is_reversed,
        orientation="reversed" if is_reversed else "upright",
    )


def format_card_details_for_prompt(card_data: list[dict[str, Any]], card_meanings: dict[str, dict[str, str]]) -> str:
    cards = [_card_like(item) for item in card_data]
    return format_card_details(cards, card_meanings)


def prepare_prompt_input(input_dict: dict[str, Any], meanings_dict: dict[str, dict[str, str]]) -> dict[str, str]:
    cards = [_card_like(item) for item in input_dict["cards"]]
    return {
        "card_details": format_card_details(cards, meanings_dict),
        "context": input_dict["context"],
        "symbolism": format_symbolism(cards, meanings_dict),
    }


def get_llm(model: str = DEFAULT_MODEL, base_url: str = DEFAULT_BASE_URL, temperature: float = 0.8) -> Any:
    return build_llm(model=model, base_url=base_url, temperature=temperature)
