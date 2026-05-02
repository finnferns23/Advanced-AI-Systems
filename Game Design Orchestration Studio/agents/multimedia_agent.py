from __future__ import annotations

from agents.base_agent import BaseGameAgent
from schemas import AgentResult, GameBrief


class MultimediaOrchestratorAgent(BaseGameAgent):
    name = "Multimedia Orchestrator Agent"
    role = "Combines text, voice, image, video, audio, dynamic, and interactive outputs into one pipeline"

    def run(self, brief: GameBrief, context: dict | None = None) -> AgentResult:

        completed = list((context or {}).get("completed_agents", []))
        outputs = {
            "integration_rules": ["Every media asset must support the core loop", "Text, voice, and captions must match", "Image and video reuse the visual bible", "Audio has visual alternatives", "Dynamic systems remain testable"],
            "media_pipeline": ["Brief", "Specialist outputs", "Style bible", "Prototype", "QA", "Pitch package"],
            "deliverables": ["Game design document", "Media prompt pack", "Prototype task board", "Accessibility checklist", "Pitch summary", "JSON package"],
            "dependencies_checked": completed,
        }
        return self.result("Multimedia orchestration aligns all specialist layers into a single production-ready game design package.", outputs, ["Disconnected media directions weaken production"], ["Review all outputs against design pillars before implementation"])
