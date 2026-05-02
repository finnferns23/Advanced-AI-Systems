"""Interpretation agent powered by Ollama through LangChain."""

from __future__ import annotations

from typing import Any, List

from core.config import DEFAULT_BASE_URL, DEFAULT_MODEL, DEFAULT_TEMPERATURE
from core.models import CardMeanings, TarotState
from tools.reading_formatter import fallback_reading


def build_llm(model: str = DEFAULT_MODEL, base_url: str = DEFAULT_BASE_URL, temperature: float = DEFAULT_TEMPERATURE) -> Any:
    """Create the Ollama chat model lazily so imports remain safe."""
    from langchain_ollama import ChatOllama

    return ChatOllama(model=model, base_url=base_url, temperature=temperature)


def build_prompt_messages(question: str, card_details: str, symbolism: str, memory_context: str) -> List[Any]:
    """Create structured chat messages for the tarot interpretation."""
    from langchain_core.messages import HumanMessage, SystemMessage

    system_content = (
        "You are Tarrow Chat Agent, an advanced reflective tarot assistant. "
        "Use the cards, orientation, symbolism, and session context to generate grounded guidance. "
        "Do not claim certainty about the future. Do not present medical, legal, financial, or professional advice as fact. "
        "Frame the result as reflection, pattern recognition, and user agency."
    )
    human_content = f"""
Question or context:
{question}

Session memory context:
{memory_context}

Drawn cards and meanings:
{card_details}

Symbolism notes:
{symbolism}

Write the reading with these sections:
1. Opening reflection
2. Card by card interpretation
3. Combined message of the spread
4. Practical next steps
5. Closing reminder that the user has agency
""".strip()
    return [SystemMessage(content=system_content), HumanMessage(content=human_content)]


def create_interpretation_agent(meanings: CardMeanings, model: str = DEFAULT_MODEL, base_url: str = DEFAULT_BASE_URL):
    """Create a LangGraph node that generates the draft interpretation."""
    try:
        from langchain_core.output_parsers import StrOutputParser

        llm = build_llm(model=model, base_url=base_url)
        parser = StrOutputParser()
    except Exception as exc:
        setup_error = str(exc)
        llm = None
        parser = None
    else:
        setup_error = ""

    def interpretation_agent(state: TarotState) -> TarotState:
        cards = state["cards"]
        if llm is None or parser is None:
            response = fallback_reading(state["question"], cards, meanings, state.get("memory_context", ""))
            return {**state, "draft_response": response, "error": setup_error}

        try:
            messages = build_prompt_messages(
                question=state["question"],
                card_details=state["card_details"],
                symbolism=state["symbolism"],
                memory_context=state.get("memory_context", "No previous readings in this session."),
            )
            response = (llm | parser).invoke(messages)
        except Exception as exc:
            response = fallback_reading(state["question"], cards, meanings, state.get("memory_context", ""))
            return {**state, "draft_response": response, "error": str(exc)}

        return {**state, "draft_response": response}

    return interpretation_agent
