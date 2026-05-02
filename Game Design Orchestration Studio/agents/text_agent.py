from __future__ import annotations

from agents.base_agent import BaseGameAgent
from schemas import AgentResult, GameBrief


class TextDesignAgent(BaseGameAgent):
    name = "Text Design Agent"
    role = "Creates narrative, UI copy, dialogue, quest text, captions, and UX writing"

    def run(self, brief: GameBrief, context: dict | None = None) -> AgentResult:

        outputs = {
            "narrative_logline": f"A focused {brief.genre.lower()} journey where {brief.theme.lower()} shapes every choice.",
            "ui_copy": {"start": "Begin Journey", "continue": "Continue", "settings": "Settings", "accessibility": "Accessibility"},
            "sample_dialogue": ["We remember the path by rebuilding it.", "Every choice leaves a signal.", "Move carefully; the world reacts."],
            "quest_templates": ["Discover the signal source", "Choose an ally", "Stabilize the area", "Return with evidence"],
            "caption_policy": ["Captions for all dialogue", "Speaker labels", "Non-speech sound captions"],
        }
        return self.result("Text system covers story, UI, dialogue, quests, captions, and player guidance.", outputs, ["Too much lore can slow onboarding"], ["Keep first-session text short and skippable"])
