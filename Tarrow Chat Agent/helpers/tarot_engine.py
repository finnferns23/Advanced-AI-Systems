"""Public engine API used by app.py and main.py."""

from __future__ import annotations

from core.config import DEFAULT_BASE_URL, DEFAULT_MODEL, IMAGE_DIR, VALID_SPREADS
from core.models import CardMeanings, SessionMemory, TarotCard, TarotState
from graph.workflow import create_tarot_workflow
from memory.session_memory import get_memory
from tools.deck_loader import load_tarot_data
from tools.reading_formatter import format_card_details, format_symbolism
from tools.spread_generator import draw_cards


def run_reading(
    question: str,
    num_cards: int = 3,
    model: str = DEFAULT_MODEL,
    base_url: str = DEFAULT_BASE_URL,
    memory: SessionMemory | None = None,
) -> TarotState:
    """Run the full advanced tarot workflow and return the final state."""
    clean_question = question.strip()
    if not clean_question:
        raise ValueError("Please provide a question or context for the reading.")

    _, meanings = load_tarot_data()
    active_memory = memory or get_memory()
    workflow = create_tarot_workflow(meanings=meanings, model=model, base_url=base_url)
    result: TarotState = workflow.invoke(
        {
            "question": clean_question,
            "num_cards": int(num_cards),
            "model": model,
            "base_url": base_url,
            "memory_context": active_memory.recent_context(),
        }
    )
    active_memory.add(clean_question, result.get("cards", []), result.get("response", ""))
    return result


__all__ = [
    "DEFAULT_BASE_URL",
    "DEFAULT_MODEL",
    "IMAGE_DIR",
    "VALID_SPREADS",
    "CardMeanings",
    "TarotCard",
    "TarotState",
    "draw_cards",
    "format_card_details",
    "format_symbolism",
    "load_tarot_data",
    "run_reading",
]
