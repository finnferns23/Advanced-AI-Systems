from __future__ import annotations


def integration_status() -> dict[str, str]:
    return {
        "status": "ready",
        "package": "langchain + langchain-community",
        "purpose": "Optional extension point for LangChain chains, prompt templates, retrievers, and RAG tools. Core app runs without importing this dependency.",
    }
