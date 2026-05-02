"""Card selection agent."""

from __future__ import annotations

from core.models import CardMeanings, TarotState
from tools.spread_generator import draw_cards


def create_card_selection_agent(meanings: CardMeanings):
    """Create a LangGraph node that draws cards for the requested spread."""
    card_names = list(meanings.keys())

    def card_selection_agent(state: TarotState) -> TarotState:
        cards = draw_cards(int(state["num_cards"]), card_names)
        return {**state, "cards": cards}

    return card_selection_agent
