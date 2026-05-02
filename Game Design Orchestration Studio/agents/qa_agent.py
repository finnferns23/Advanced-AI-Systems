from __future__ import annotations

from agents.base_agent import BaseGameAgent
from schemas import AgentResult, GameBrief


class QaAndSafetyAgent(BaseGameAgent):
    name = "QA and Safety Agent"
    role = "Checks feasibility, hallucination risk, accessibility, platform readiness, and portfolio quality"

    def run(self, brief: GameBrief, context: dict | None = None) -> AgentResult:

        outputs = {
            "qa_checks": ["No fake statistics", "Planned features labelled as planned", "Offline mode available", "API failures handled safely", "Outputs saved as Markdown and JSON"],
            "accessibility_checks": ["Captions", "Keyboard support", "Color-independent cues", "Audio alternatives", "Readable UI copy", "Remappable controls planned"],
            "risk_register": ["Scope creep", "Media inconsistency", "Unverified tool claims", "Overpromised trailer content"],
            "definition_of_done": ["CLI runs", "Streamlit runs", "Compile check passes", "Pytest passes", "No secrets or cache files committed"],
        }
        return self.result("QA review focuses on reliability, accessibility, feasibility, and anti-hallucination safeguards.", outputs, ["Testing with real players is still required"], ["Run smoke tests after each major change"])
