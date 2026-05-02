from __future__ import annotations

from typing import Any

from agents.audio_agent import AudioAgent
from agents.concept_agent import ConceptAgent
from agents.dynamic_agent import DynamicSystemsAgent
from agents.image_agent import ImageAgent
from agents.interactive_agent import InteractivePrototypeAgent
from agents.multimedia_agent import MultimediaOrchestratorAgent
from agents.pitch_agent import PitchAgent
from agents.qa_agent import QaAndSafetyAgent
from agents.text_agent import TextDesignAgent
from agents.video_agent import VideoAgent
from agents.voice_agent import VoiceAgent
from schemas import AgentResult, DesignPackage, GameBrief


class GameDesignOrchestrator:
    """Deterministic multi-agent workflow for a production-safe portfolio project."""

    def __init__(self) -> None:
        self.agents = [
            ConceptAgent(),
            TextDesignAgent(),
            VoiceAgent(),
            ImageAgent(),
            AudioAgent(),
            VideoAgent(),
            DynamicSystemsAgent(),
            InteractivePrototypeAgent(),
            MultimediaOrchestratorAgent(),
            QaAndSafetyAgent(),
            PitchAgent(),
        ]

    def run(self, brief: GameBrief) -> DesignPackage:
        clean_brief = brief.sanitized()
        results: list[AgentResult] = []
        context: dict[str, Any] = {"brief": clean_brief.to_dict(), "completed_agents": []}
        for agent in self.agents:
            result = agent.run(clean_brief, context)
            results.append(result)
            context[agent.name] = result.outputs
            context["completed_agents"].append(agent.name)

        combined_summary = (
            f"{clean_brief.title} design package completed with {len(results)} specialist agents "
            "covering concept, text, voice, image, audio, video, dynamic systems, interactive prototype, multimedia orchestration, QA, and pitch."
        )
        production_plan = {
            "recommended_repo": "Advanced-AI-Systems/Game-Design-Agent-Team",
            "runtime_modes": ["offline deterministic mode", "optional OpenAI live mode"],
            "extension_points": ["OpenAI", "LangChain", "LangGraph", "Agno", "AutoGen"],
            "phases": [
                "Lock concept and pillars",
                "Generate text, voice, image, audio, and video media bible",
                "Design dynamic systems and prototype loop",
                "Run QA, accessibility, and feasibility checks",
                "Prepare pitch and GitHub portfolio demo",
            ],
            "anti_hallucination_rules": [
                "Do not invent market data",
                "Label planned features clearly",
                "Use deterministic fallback when APIs fail",
                "Validate outputs before saving",
            ],
        }
        return DesignPackage(clean_brief, results, combined_summary, production_plan)
