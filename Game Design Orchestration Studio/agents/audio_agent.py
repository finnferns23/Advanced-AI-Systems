from __future__ import annotations

from agents.base_agent import BaseGameAgent
from schemas import AgentResult, GameBrief


class AudioAgent(BaseGameAgent):
    name = "Audio Agent"
    role = "Designs music, SFX, ambience, adaptive audio, and non-audio alternatives"

    def run(self, brief: GameBrief, context: dict | None = None) -> AgentResult:

        outputs = {
            "music_direction": ["Low-fatigue menu loop", "Adaptive exploration layer", "Tension layer for risk moments", "Short success sting"],
            "sfx_catalog": ["Confirm", "Cancel", "Objective discovered", "Hazard nearby", "Reward", "Low resource", "Checkpoint"],
            "adaptive_rules": ["Layer tension when world_tension rises", "Reduce density during dialogue", "Use short cues for repeated actions"],
            "audio_accessibility": ["Visual alternatives for critical sounds", "Volume sliders by category", "Mono audio support", "Caption non-speech sounds"],
        }
        return self.result("Audio plan covers music, SFX, ambience, adaptive behavior, and accessibility.", outputs, ["Audio cues cannot be the only feedback channel"], ["Prototype audio states with placeholders first"])
