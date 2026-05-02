from __future__ import annotations

from config import settings


class SafeLLMClient:
    """Safe optional LLM wrapper.

    Offline deterministic mode is the default, so the project runs on GitHub,
    Streamlit Community Cloud, interviews, and local machines without API keys.
    """

    def __init__(self, timeout_seconds: int | None = None) -> None:
        self.timeout_seconds = timeout_seconds or settings.llm_timeout_seconds

    def generate(self, system_prompt: str, user_prompt: str, fallback: str) -> str:
        if not settings.use_live_llm or not settings.openai_api_key:
            return fallback
        try:
            from openai import OpenAI
            client = OpenAI(api_key=settings.openai_api_key, timeout=self.timeout_seconds)
            response = client.chat.completions.create(
                model=settings.model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.35,
            )
            content = response.choices[0].message.content
            return content.strip() if content else fallback
        except Exception as exc:  # noqa: BLE001 - safe fallback for demo reliability
            return f"{fallback}\n\nOptional live LLM call was skipped safely: {exc}"
