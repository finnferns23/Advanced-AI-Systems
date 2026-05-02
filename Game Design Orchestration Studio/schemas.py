from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


class GameBrief:
    defaults = {
        "title": "Echoes of Ember",
        "genre": "Action Adventure",
        "audience": "Indie PC and console players",
        "platform": "PC",
        "theme": "Memory, survival, and discovery",
        "constraints": "Prototype-first, accessible, realistic indie scope",
        "target_rating": "Teen",
        "monetization": "Premium indie release",
    }

    def __init__(
        self,
        title: str = defaults["title"],
        genre: str = defaults["genre"],
        audience: str = defaults["audience"],
        platform: str = defaults["platform"],
        theme: str = defaults["theme"],
        constraints: str = defaults["constraints"],
        target_rating: str = defaults["target_rating"],
        monetization: str = defaults["monetization"],
    ) -> None:
        self.title = title
        self.genre = genre
        self.audience = audience
        self.platform = platform
        self.theme = theme
        self.constraints = constraints
        self.target_rating = target_rating
        self.monetization = monetization

    def sanitized(self) -> "GameBrief":
        data = self.to_dict()
        clean = {key: (str(value).strip() or self.defaults[key]) for key, value in data.items()}
        return GameBrief(**clean)

    def to_dict(self) -> dict[str, str]:
        return {
            "title": self.title,
            "genre": self.genre,
            "audience": self.audience,
            "platform": self.platform,
            "theme": self.theme,
            "constraints": self.constraints,
            "target_rating": self.target_rating,
            "monetization": self.monetization,
        }


class AgentResult:
    def __init__(
        self,
        agent_name: str,
        role: str,
        summary: str,
        outputs: dict[str, Any] | None = None,
        risks: list[str] | None = None,
        next_steps: list[str] | None = None,
        assumptions: list[str] | None = None,
    ) -> None:
        self.agent_name = agent_name
        self.role = role
        self.summary = summary
        self.outputs = outputs or {}
        self.risks = risks or []
        self.next_steps = next_steps or []
        self.assumptions = assumptions or []

    def to_dict(self) -> dict[str, Any]:
        return {
            "agent_name": self.agent_name,
            "role": self.role,
            "summary": self.summary,
            "outputs": self.outputs,
            "risks": self.risks,
            "next_steps": self.next_steps,
            "assumptions": self.assumptions,
        }


class DesignPackage:
    def __init__(
        self,
        brief: GameBrief,
        results: list[AgentResult],
        combined_summary: str,
        production_plan: dict[str, Any],
    ) -> None:
        self.brief = brief
        self.results = results
        self.combined_summary = combined_summary
        self.production_plan = production_plan
        self.created_at_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    def to_dict(self) -> dict[str, Any]:
        return {
            "brief": self.brief.to_dict(),
            "results": [result.to_dict() for result in self.results],
            "combined_summary": self.combined_summary,
            "production_plan": self.production_plan,
            "created_at_utc": self.created_at_utc,
        }
