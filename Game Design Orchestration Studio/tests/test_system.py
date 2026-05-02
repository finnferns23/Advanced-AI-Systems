from schemas import GameBrief
from tools.validators import REQUIRED_AGENTS, validate_package
from workflows.orchestrator import GameDesignOrchestrator


def test_orchestrator_generates_complete_package():
    brief = GameBrief("Test Game", "Puzzle", "PC players", "PC", "Logic", "Small scope")
    package = GameDesignOrchestrator().run(brief)
    assert len(package.results) == len(REQUIRED_AGENTS)
    assert validate_package(package) == []
    assert REQUIRED_AGENTS == {result.agent_name for result in package.results}


def test_outputs_are_structured():
    package = GameDesignOrchestrator().run(GameBrief())
    data = package.to_dict()
    assert data["brief"]["title"]
    assert data["production_plan"]["recommended_repo"] == "Advanced-AI-Systems/Game-Design-Agent-Team"
