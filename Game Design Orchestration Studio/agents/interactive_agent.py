from __future__ import annotations

from agents.base_agent import BaseGameAgent
from schemas import AgentResult, GameBrief


class InteractivePrototypeAgent(BaseGameAgent):
    name = "Interactive Prototype Agent"
    role = "Turns the design into screens, controls, MVP tasks, and playable prototype scope"

    def run(self, brief: GameBrief, context: dict | None = None) -> AgentResult:

        outputs = {
            "mvp_screens": ["Start", "Settings", "Accessibility", "Playable scene", "Result summary"],
            "input_model": ["Keyboard", "Controller-ready actions", "Mouse optional", "Remappable controls planned"],
            "prototype_scope": ["One playable loop", "Placeholder assets", "Basic state tracking", "No final art dependency"],
            "task_board": ["Greybox scene", "Movement/input", "Interaction trigger", "Feedback layer", "Result screen", "Usability test"],
            "acceptance_criteria": ["Player can start without instructions from developer", "Failure and success are understandable", "Settings are reachable"],
        }
        return self.result("Interactive plan defines a playable MVP, screens, controls, task board, and acceptance criteria.", outputs, ["Polishing too early can hide weak mechanics"], ["Build greybox first, then layer media"])
