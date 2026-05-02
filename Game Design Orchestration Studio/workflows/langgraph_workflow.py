from __future__ import annotations

from schemas import DesignPackage, GameBrief
from workflows.orchestrator import GameDesignOrchestrator


def run_langgraph_ready_workflow(brief: GameBrief) -> DesignPackage:
    """Stable fallback workflow with the same public shape as a LangGraph workflow.

    This keeps the project runnable even when LangGraph is not installed. When deploying
    with LangGraph, replace this wrapper with graph nodes that call the same agents.
    """
    return GameDesignOrchestrator().run(brief)
