# Game Design Agent Team - Advanced AI System

A clean, portfolio-ready multi-agent system that turns one game brief into an end-to-end game design package. It covers concept design, text, voice, image, audio, video, dynamic game systems, interactive prototype planning, multimedia orchestration, QA, accessibility, anti-hallucination checks, and pitch material.

## Recommended GitHub Location

```text
Advanced-AI-Systems/Game-Design-Agent-Team
```

Use this under **Advanced AI Systems** because it includes specialist agents, workflow orchestration, optional LLM/framework extension points, validation, CLI execution, and a Streamlit interface.

## Agents Included

- **Concept Agent**: hook, player fantasy, pillars, scope, and success metrics
- **Text Design Agent**: narrative, UI copy, dialogue, quest text, captions, and UX writing
- **Voice Agent**: narration, character barks, TTS planning, localization, and accessibility
- **Image Agent**: art direction, visual bible, asset list, and image-generation prompts
- **Audio Agent**: music, SFX, ambience, adaptive audio, and non-audio alternatives
- **Video Agent**: trailer structure, cutscenes, gameplay capture, and video prompts
- **Dynamic Systems Agent**: core loop, progression, economy, difficulty, and state variables
- **Interactive Prototype Agent**: screens, controls, MVP task board, and acceptance criteria
- **Multimedia Orchestrator Agent**: combines all specialist layers into one production pipeline
- **QA and Safety Agent**: feasibility, accessibility, reliability, and anti-hallucination review
- **Pitch Agent**: elevator pitch, roadmap, monetization, demo script, and GitHub positioning

## Folder Structure

```text
Game_Design_Agent_Team/
├── agents/
│   ├── base_agent.py
│   ├── concept_agent.py
│   ├── text_agent.py
│   ├── voice_agent.py
│   ├── image_agent.py
│   ├── audio_agent.py
│   ├── video_agent.py
│   ├── dynamic_agent.py
│   ├── interactive_agent.py
│   ├── multimedia_agent.py
│   ├── qa_agent.py
│   └── pitch_agent.py
├── workflows/
│   ├── orchestrator.py
│   └── langgraph_workflow.py
├── integrations/
│   ├── openai_adapter.py
│   ├── langchain_adapter.py
│   ├── agno_adapter.py
│   └── autogen_adapter.py
├── tools/
│   ├── report_builder.py
│   └── validators.py
├── memory/
│   └── design_memory.py
├── tests/
│   └── test_system.py
├── app.py
├── main.py
├── config.py
├── llm_client.py
├── schemas.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Architecture Flow

```text
GameBrief
   ↓
Concept Agent
   ↓
Text + Voice + Image + Audio + Video Agents
   ↓
Dynamic Systems Agent
   ↓
Interactive Prototype Agent
   ↓
Multimedia Orchestrator Agent
   ↓
QA and Safety Agent
   ↓
Pitch Agent
   ↓
Markdown Report + JSON Package
```

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Conda option:

```bash
conda create -n game-design-agent python=3.11 -y
conda activate game-design-agent
pip install -r requirements.txt
```

## Run CLI

```bash
python main.py
```

Custom brief:

```bash
python main.py --title "Neon Kingdom" --genre "RPG" --platform "PC" --theme "Cyber fantasy rebellion" --constraints "Small indie prototype"
```

Generated files are created locally in:

```text
outputs/game_design_report.md
outputs/game_design_package.json
```

The `outputs` folder is intentionally not included in the repository zip; it is created automatically when you run the project.

## Run Streamlit App

```bash
streamlit run app.py
```

## Optional OpenAI Mode

The project runs offline by default. To enable live OpenAI mode:

```text
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4.1-mini
USE_LIVE_LLM=true
```

The app has deterministic fallback behavior, so API errors do not break demos.

## Framework Extension Points

Safe extension files are included for:

- OpenAI
- LangChain
- LangGraph
- Agno
- AutoGen 0.4+ using `autogen-agentchat` and `autogen-ext[openai]`

The normal runtime does not import heavy optional frameworks unless you extend the adapters. This keeps the CLI and Streamlit app stable.

## Anti-Hallucination and Reliability

This system avoids overclaiming by:

- Not inventing market numbers or external facts
- Labelling planned features as planned
- Using deterministic fallback outputs
- Validating required agents before saving files
- Keeping optional API integrations isolated
- Including QA and accessibility checks in the workflow

## Testing and Validation

```bash
python -m compileall .
pytest
python main.py
```

Expected result:

- Compile check passes
- Tests pass
- CLI creates Markdown and JSON outputs
- Streamlit launches with `streamlit run app.py`

## GitHub Checklist

- Keep `.env` out of GitHub
- Do not commit virtual environments
- Do not commit `__pycache__`
- Do not commit generated reports or media unless needed for demo proof
- Run `python -m compileall .`
- Run `pytest`
- Run `python main.py`

## Portfolio Summary

This project demonstrates an advanced AI system for game design using multi-agent decomposition, multimedia planning, safe orchestration, optional AI framework integration, validation, and a Streamlit interface. It is suitable for GitHub, portfolio presentation, and interview discussion.
