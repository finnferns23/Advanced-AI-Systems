from __future__ import annotations

from agents.base_agent import BaseGameAgent
from schemas import AgentResult, GameBrief


class VoiceAgent(BaseGameAgent):
    name = "Voice Agent"
    role = "Plans narration, character barks, voice direction, TTS, localization, and accessibility"

    def run(self, brief: GameBrief, context: dict | None = None) -> AgentResult:

        outputs = {
            "voice_direction": ["Warm but tense narrator", "Short reactive character barks", "Clean pronunciation for screen-reader compatibility"],
            "tts_plan": ["Use text fallback for every spoken line", "Avoid voice-only instructions", "Keep lines short for re-recording"],
            "character_barks": ["Careful.", "That changed something.", "We have a route.", "Try a different angle."],
            "localization_notes": ["Avoid idioms in critical instructions", "Keep variable placeholders clear", "Separate subtitles from UI strings"],
        }
        return self.result("Voice layer supports narration, character feedback, TTS planning, and accessible captions.", outputs, ["Voice-only cues can exclude players"], ["Create a voice-line spreadsheet before recording"])
