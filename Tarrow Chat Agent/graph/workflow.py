"""LangGraph orchestration workflow for the advanced tarot system."""

from __future__ import annotations

from agents.card_selection_agent import create_card_selection_agent
from agents.context_reasoning_agent import create_context_reasoning_agent
from agents.interpretation_agent import create_interpretation_agent
from agents.validation_agent import validation_agent
from core.config import DEFAULT_BASE_URL, DEFAULT_MODEL
from core.models import CardMeanings, TarotState


class FallbackWorkflow:
    """Small fallback runner used when LangGraph is not installed."""

    def __init__(self, nodes):
        self.nodes = nodes

    def invoke(self, state: TarotState) -> TarotState:
        current_state = state
        for node in self.nodes:
            current_state = node(current_state)
        return current_state


def create_tarot_workflow(meanings: CardMeanings, model: str = DEFAULT_MODEL, base_url: str = DEFAULT_BASE_URL):
    """Build the advanced agent workflow with LangGraph."""
    nodes = [
        create_card_selection_agent(meanings),
        create_context_reasoning_agent(meanings),
        create_interpretation_agent(meanings, model=model, base_url=base_url),
        validation_agent,
    ]

    try:
        from langgraph.graph import END, StateGraph
    except Exception:
        return FallbackWorkflow(nodes)

    workflow = StateGraph(TarotState)
    workflow.add_node("card_selection_agent", nodes[0])
    workflow.add_node("context_reasoning_agent", nodes[1])
    workflow.add_node("interpretation_agent", nodes[2])
    workflow.add_node("validation_agent", nodes[3])

    workflow.set_entry_point("card_selection_agent")
    workflow.add_edge("card_selection_agent", "context_reasoning_agent")
    workflow.add_edge("context_reasoning_agent", "interpretation_agent")
    workflow.add_edge("interpretation_agent", "validation_agent")
    workflow.add_edge("validation_agent", END)
    return workflow.compile()
