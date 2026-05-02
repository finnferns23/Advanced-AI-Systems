"""Context reasoning agent."""

from __future__ import annotations

from core.models import CardMeanings, TarotState
from tools.reading_formatter import format_card_details, format_symbolism


def create_context_reasoning_agent(meanings: CardMeanings):
    """Create a LangGraph node that prepares card meanings, symbolism, and memory context."""

    def context_reasoning_agent(state: TarotState) -> TarotState:
        cards = state["cards"]
        memory_context = state.get("memory_context") or "No previous readings in this session."
        return {
            **state,
            "card_details": format_card_details(cards, meanings),
            "symbolism": format_symbolism(cards, meanings),
            "memory_context": memory_context,
        }

    return context_reasoning_agent
