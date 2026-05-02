"""Streamlit app for the advanced Tarrow Chat Agent."""

from __future__ import annotations

from typing import Any

import streamlit as st

from core.config import DEFAULT_BASE_URL, DEFAULT_MODEL, IMAGE_DIR
from helpers.tarot_engine import load_tarot_data, run_reading
from memory.session_memory import get_memory
from tools.image_mapper import load_card_image


st.set_page_config(
    page_title="Tarrow Chat Agent",
    page_icon="🃏",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_data(show_spinner=False)
def get_tarot_dataset():
    """Load tarot data once per Streamlit session."""
    return load_tarot_data()


def show_card(card: Any, index: int) -> None:
    """Render one tarot card with image and orientation."""
    st.markdown(f"#### Card {index}")
    st.caption(f"{card.name} · {card.orientation.title()}")
    image = load_card_image(card.image_path, card.is_reversed)
    if image is not None:
        st.image(image, use_container_width=True)
    else:
        st.warning(f"Image missing: {IMAGE_DIR / card.name}")


def render_history() -> None:
    """Display previous readings during the current Streamlit session."""
    history = st.session_state.get("reading_history", [])
    if not history:
        return

    with st.expander("Session reading history"):
        for item_index, item in enumerate(reversed(history[-5:]), start=1):
            st.markdown(f"**Reading {item_index}:** {item['question']}")
            st.caption(", ".join(item["cards"]))


def main() -> None:
    """Run the Streamlit user interface."""
    st.title("Tarrow Chat Agent")
    st.markdown(
        "An advanced AI system using modular agents, LangGraph orchestration, "
        "session memory, reusable tools, Ollama, LangChain, and Streamlit."
    )

    with st.sidebar:
        st.header("Reading setup")
        num_cards = st.selectbox("Choose spread size", options=[3, 5, 7], index=0)
        model = st.text_input("Ollama model", value=DEFAULT_MODEL)
        base_url = st.text_input("Ollama base URL", value=DEFAULT_BASE_URL)
        st.divider()
        st.markdown("**Local setup**")
        st.code("ollama pull phi4\nollama serve", language="bash")
        st.caption("If Ollama is not running, the app returns a local fallback reading.")

    try:
        _, meanings = get_tarot_dataset()
        st.caption(f"Loaded {len(meanings)} cards from data/tarots.csv")
    except Exception as exc:
        st.error(f"Could not load the tarot dataset: {exc}")
        return

    question = st.text_area(
        "Enter your question or context",
        placeholder="Example: What should I reflect on before making my next career decision?",
        height=130,
    )

    col_a, col_b = st.columns([1, 4])
    with col_a:
        draw_button = st.button("Draw cards", type="primary", use_container_width=True)
    with col_b:
        st.caption("This reading is reflective guidance and not a fixed prediction.")

    render_history()

    if not draw_button:
        st.markdown("Use the sidebar to choose your spread, then enter a question to begin.")
        return

    clean_question = question.strip()
    if not clean_question:
        st.warning("Please enter a question or context before drawing cards.")
        return

    with st.spinner("Running the advanced agent workflow..."):
        result = run_reading(
            question=clean_question,
            num_cards=num_cards,
            model=model,
            base_url=base_url,
            memory=get_memory(),
        )

    cards = result.get("cards", [])
    st.session_state.setdefault("reading_history", []).append(
        {
            "question": clean_question,
            "cards": [f"{card.name} ({card.orientation})" for card in cards],
        }
    )

    st.subheader("Your cards")
    if cards:
        columns = st.columns(len(cards))
        for index, card in enumerate(cards, start=1):
            with columns[index - 1]:
                show_card(card, index)
    else:
        st.warning("No cards were drawn.")

    st.subheader("Interpretation")
    if result.get("error"):
        st.warning("Ollama was not reachable, so the app returned a local fallback reading.")
        with st.expander("Technical details"):
            st.code(result["error"])

    st.markdown(result.get("response", "No reading was generated."))

    with st.expander("Advanced workflow details"):
        st.markdown("**Validation notes**")
        st.write(result.get("validation_notes", "No validation notes available."))
        st.markdown("**Card details used for the reading**")
        st.text(result.get("card_details", "No card details available."))
        st.markdown("**Memory context**")
        st.text(result.get("memory_context", "No memory context available."))


if __name__ == "__main__":
    main()
