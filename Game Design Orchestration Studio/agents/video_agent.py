from __future__ import annotations

from agents.base_agent import BaseGameAgent
from schemas import AgentResult, GameBrief


class VideoAgent(BaseGameAgent):
    name = "Video Agent"
    role = "Plans trailers, cutscenes, gameplay capture, video prompts, and editing structure"

    def run(self, brief: GameBrief, context: dict | None = None) -> AgentResult:

        outputs = {
            "trailer_structure": ["0-5s hook", "5-15s player fantasy", "15-30s core loop", "30-45s escalation", "45-60s title and CTA"],
            "cutscene_policy": ["Short scenes", "Skippable", "Subtitled", "No essential info only in video"],
            "video_prompts": [
                f"Short trailer shot list for {brief.title}, {brief.genre}, {brief.theme}, gameplay-first pacing",
                f"Cinematic reveal sequence for {brief.title}, accessible captions, no fast unreadable text",
            ],
            "capture_checklist": ["Record core loop", "Record menu/accessibility settings", "Record failure and success states", "Export short portfolio clip"],
        }
        return self.result("Video plan converts the design into trailer, cutscene, and portfolio capture guidance.", outputs, ["Trailer can overpromise unbuilt systems"], ["Only show implemented or clearly labelled prototype footage"])
