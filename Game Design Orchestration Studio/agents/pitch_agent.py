from __future__ import annotations

from agents.base_agent import BaseGameAgent
from schemas import AgentResult, GameBrief


class PitchAgent(BaseGameAgent):
    name = "Pitch Agent"
    role = "Creates stakeholder-ready pitch, roadmap, monetization, demo plan, and GitHub positioning"

    def run(self, brief: GameBrief, context: dict | None = None) -> AgentResult:

        outputs = {
            "elevator_pitch": f"{brief.title} is a focused {brief.genre.lower()} experience built around {brief.theme.lower()}, designed with coordinated text, voice, image, audio, video, dynamic, and interactive systems.",
            "roadmap": ["Phase 1: Core loop", "Phase 2: Media bible", "Phase 3: Playable prototype", "Phase 4: QA/accessibility", "Phase 5: Portfolio demo"],
            "monetization_fit": [brief.monetization, "Optional soundtrack/artbook", "Avoid pay-to-win mechanics"],
            "github_positioning": "Advanced-AI-Systems/Game-Design-Agent-Team",
            "demo_script": ["Show brief form", "Generate package", "Open report", "Review agent outputs", "Download JSON"],
        }
        return self.result("Pitch package prepares the project for GitHub, interviews, stakeholders, and portfolio demos.", outputs, ["Do not claim generated plans are implemented game assets"], ["Add real prototype screenshots after implementation"])
