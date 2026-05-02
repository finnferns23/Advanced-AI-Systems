from __future__ import annotations

from typing import Any

from llm_client import SafeLLMClient
from schemas import AgentResult, GameBrief


class BaseGameAgent:
    name = "Base Agent"
    role = "Generic specialist"

    def __init__(self, llm: SafeLLMClient | None = None) -> None:
        self.llm = llm or SafeLLMClient()

    def result(
        self,
        summary: str,
        outputs: dict[str, Any],
        risks: list[str] | None = None,
        next_steps: list[str] | None = None,
        assumptions: list[str] | None = None,
    ) -> AgentResult:
        return AgentResult(
            agent_name=self.name,
            role=self.role,
            summary=summary,
            outputs=outputs,
            risks=risks or [],
            next_steps=next_steps or [],
            assumptions=assumptions or [],
        )

    def run(self, brief: GameBrief, context: dict[str, Any] | None = None) -> AgentResult:
        raise NotImplementedError
