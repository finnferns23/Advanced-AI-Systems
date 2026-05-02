"""Validation and response refinement agent."""

from __future__ import annotations

from core.models import TarotState


def validation_agent(state: TarotState) -> TarotState:
    """Finalize the response and add a safety note if needed."""
    draft = state.get("draft_response", "No reading was generated.").strip()
    safety_note = (
        "\n\nNote: This reading is for reflection and personal insight only. "
        "Use your own judgement for real-world decisions."
    )
    response = draft if "reflection" in draft.lower() or "agency" in draft.lower() else draft + safety_note
    return {**state, "response": response, "validation_notes": "Response finalized with reflective guidance framing."}
