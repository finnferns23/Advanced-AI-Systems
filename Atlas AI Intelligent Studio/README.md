# Atlas AI Intelligent Studio

Production-focused AI workspace for assistants, document knowledge, image reasoning, voice output, and MCP planning.

## Purpose

Atlas AI Intelligent Studio is a single unified Streamlit application with a clean service layer under `src/atlas_ai_intelligent_studio`. It is designed for professional portfolio use, local experimentation, and future extension inside an `advanced-ai-systems` GitHub repository.

## Capabilities

- General AI assistant workflow
- Document knowledge base for TXT, Markdown, and PDF uploads
- Retrieval-based answers from uploaded session documents
- Image reasoning with a user question
- MP3 voice output from generated or pasted text
- MCP configuration dry-check and command hint
- Diagnostics dashboard for local validation flags
- Windows run and validation scripts
- Core tests for retrieval, configuration, file handling, and MCP checks

## Folder structure

```text
atlas_ai_intelligent_studio/
├── app.py
├── src/atlas_ai_intelligent_studio/
│   ├── __init__.py
│   ├── assistant.py
│   ├── config.py
│   ├── ingest.py
│   ├── mcp.py
│   ├── rag.py
│   └── text.py
├── tests/
│   └── test_core.py
├── config/
│   └── mcp_agent.config.yaml
├── scripts/
│   └── validate.cmd
├── .env.example
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── run_app.cmd
```

## Setup on Windows

```cmd
cd atlas_ai_intelligent_studio
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
notepad .env
streamlit run app.py
```

## Validate

```cmd
scripts\validate.cmd
```

## Recommended GitHub location

```text
advanced-ai-systems/
└── ai_assistants/
    └── atlas_ai_intelligent_studio/
```
