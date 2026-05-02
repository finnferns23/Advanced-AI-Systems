from __future__ import annotations

from agents.base_agent import BaseGameAgent
from schemas import AgentResult, GameBrief


class ConceptAgent(BaseGameAgent):
    name = "Concept Agent"
    role = "Defines the game hook, fantasy, pillars, scope, and success criteria"

    def run(self, brief: GameBrief, context: dict | None = None) -> AgentResult:

        hook = f"{brief.title} is a {brief.genre.lower()} about {brief.theme.lower()} for {brief.audience}."
        outputs = {
            "core_hook": hook,
            "player_fantasy": f"Feel like the decisive hero inside a readable {brief.genre.lower()} system.",
            "design_pillars": ["Immediate readability", "Meaningful choices", "Strong media identity", "Prototype-first delivery"],
            "success_metrics": ["Core loop is clear in 30 seconds", "First prototype works with placeholder assets", "Every media layer supports gameplay"],
            "scope_boundaries": [brief.constraints, "No unsupported claims or fake market numbers", "Planned features are labelled as planned"],
        }
        return self.result(hook, outputs, ["Over-scoping before the fun is proven"], ["Validate the hook as a one-page concept brief"], ["No external market research was used"])
