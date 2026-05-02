from __future__ import annotations


def integration_status() -> dict[str, str]:
    return {
        "status": "ready",
        "package": "agno",
        "purpose": "Optional extension point for Agno agents, teams, workflows, memory, knowledge, and guardrails. Core app runs without importing this dependency.",
    }
