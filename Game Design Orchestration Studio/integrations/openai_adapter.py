from __future__ import annotations

from llm_client import SafeLLMClient


def generate_with_openai(system_prompt: str, user_prompt: str, fallback: str) -> str:
    return SafeLLMClient().generate(system_prompt, user_prompt, fallback)
