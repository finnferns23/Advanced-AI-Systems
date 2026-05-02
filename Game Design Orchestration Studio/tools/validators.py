from __future__ import annotations

from schemas import DesignPackage


REQUIRED_AGENTS = {
    "Concept Agent",
    "Text Design Agent",
    "Voice Agent",
    "Image Agent",
    "Audio Agent",
    "Video Agent",
    "Dynamic Systems Agent",
    "Interactive Prototype Agent",
    "Multimedia Orchestrator Agent",
    "QA and Safety Agent",
    "Pitch Agent",
}


def validate_package(package: DesignPackage) -> list[str]:
    issues: list[str] = []
    if not package.brief.title.strip():
        issues.append("Game title is required")
    agent_names = {result.agent_name for result in package.results}
    missing = sorted(REQUIRED_AGENTS - agent_names)
    if missing:
        issues.append("Missing agents: " + ", ".join(missing))
    for result in package.results:
        if not result.summary.strip():
            issues.append(f"{result.agent_name} has an empty summary")
        if not isinstance(result.outputs, dict) or not result.outputs:
            issues.append(f"{result.agent_name} has no structured outputs")
    return issues
