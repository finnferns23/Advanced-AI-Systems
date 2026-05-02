from __future__ import annotations

from agents.base_agent import BaseGameAgent
from schemas import AgentResult, GameBrief


class DynamicSystemsAgent(BaseGameAgent):
    name = "Dynamic Systems Agent"
    role = "Designs game loop, state variables, progression, balancing, economy, and difficulty"

    def run(self, brief: GameBrief, context: dict | None = None) -> AgentResult:

        outputs = {
            "core_loop": ["Explore", "Decide", "React", "Gain feedback", "Upgrade", "Retry"],
            "state_variables": ["player_skill", "world_tension", "resource_pressure", "story_alignment", "accessibility_profile"],
            "difficulty_model": ["Start fixed", "Add assist options", "Adapt only after measurable patterns", "Never punish accessibility settings"],
            "progression": ["Unlock mechanics gradually", "Reward mastery", "Keep early loop testable in one scene"],
            "economy": ["Small resource set", "No grinding-first design", "Reward exploration and skill"],
        }
        return self.result("Dynamic systems define loops, progression, difficulty, state, and balancing rules.", outputs, ["Too many variables make balancing hard"], ["Implement state logging before adaptive difficulty"])
