# Tarrow Chat Agent

Tarrow Chat Agent is an advanced multi-agent AI system for reflective tarot readings. It uses a clean agent architecture, LangGraph orchestration, LangChain with Ollama, Streamlit, reusable tools, and session memory while preserving the original tarot CSV and image assets.

The default local model is `phi4` through Ollama.

## Why This Fits Advanced AI Systems

This version is structured as a complete AI system rather than a basic chatbot. It includes:

- Modular specialist agents
- LangGraph workflow orchestration
- Shared state across the full pipeline
- Session memory for recent readings
- Reusable tool layer
- CLI and Streamlit entry points
- Safe local fallback when Ollama is unavailable
- Preserved original tarot CSV and image deck

## Agent Workflow

```text
User Question
    ↓
Card Selection Agent
    ↓
Context Reasoning Agent
    ↓
Interpretation Agent
    ↓
Validation Agent
    ↓
Final Reflective Reading
```

## Project Structure

```text
Tarrow-Chat-Agent/
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── .gitattributes
│
├── agents/
│   ├── __init__.py
│   ├── card_selection_agent.py
│   ├── context_reasoning_agent.py
│   ├── interpretation_agent.py
│   └── validation_agent.py
│
├── core/
│   ├── __init__.py
│   ├── config.py
│   └── models.py
│
├── graph/
│   ├── __init__.py
│   └── workflow.py
│
├── memory/
│   ├── __init__.py
│   └── session_memory.py
│
├── tools/
│   ├── __init__.py
│   ├── deck_loader.py
│   ├── image_mapper.py
│   ├── reading_formatter.py
│   └── spread_generator.py
│
├── helpers/
│   ├── __init__.py
│   ├── help_func.py
│   └── tarot_engine.py
│
├── data/
│   ├── tarots.csv
│   └── readme/
│       └── TheMagicianAI.gif
│
└── images/
    └── 78 tarot card images
```

## Main Components

### `app.py`

Runs the Streamlit interface. It lets the user select a spread, enter a question, view card images, receive the interpretation, and inspect workflow details.

### `main.py`

Runs the same advanced workflow from the terminal.

### `agents/`

Contains each specialist agent as a separate Python file:

- `card_selection_agent.py` draws cards from the original deck.
- `context_reasoning_agent.py` prepares meanings, symbolism, and memory context.
- `interpretation_agent.py` generates the reading using Ollama through LangChain.
- `validation_agent.py` finalizes the response with reflective framing.

### `tools/`

Contains reusable tools for loading the deck, generating spreads, formatting readings, and mapping card images.

### `graph/workflow.py`

Builds the LangGraph workflow and includes a safe fallback workflow if LangGraph is unavailable.

### `memory/session_memory.py`

Provides simple session memory for recent readings.

### `helpers/tarot_engine.py`

Public engine API used by both `app.py` and `main.py`.

## Requirements

- Python 3.10 or higher
- Ollama installed locally
- `phi4` model pulled in Ollama

Install Python packages:

```bash
pip install -r requirements.txt
```

Pull the Ollama model:

```bash
ollama pull phi4
```

Start Ollama:

```bash
ollama serve
```

## Run the Streamlit App

```bash
streamlit run app.py
```

## Run from Terminal

```bash
python main.py "What should I focus on this week?"
```

Optional arguments:

```bash
python main.py "What should I focus on this week?" --cards 5 --model phi4 --base-url http://localhost:11434
```

Supported spread sizes:

- 3 cards
- 5 cards
- 7 cards

## Validation Completed

- Python syntax check passed for all Python files
- `main.py` tested successfully in fallback mode
- `app.py` imports successfully
- Original `data/tarots.csv` retained without modification
- Original `data/readme/TheMagicianAI.gif` retained
- Original 78 tarot image files retained without modification
- Card image path fallback retained for the original Strength card naming mismatch
- Agent, tools, graph, memory, core, helpers, app, and main files are connected
- Cache folders and runtime junk excluded from the final package

## Important Note

This app is for reflection and personal insight only. It should not be treated as medical, legal, financial, professional, or fixed predictive advice.
