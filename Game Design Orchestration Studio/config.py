from __future__ import annotations

import os
from pathlib import Path


class Settings:
    def __init__(self) -> None:
        self.app_name = "Game Design Agent Team"
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
        self.use_live_llm = os.getenv("USE_LIVE_LLM", "false").lower() == "true"
        self.llm_timeout_seconds = int(os.getenv("LLM_TIMEOUT_SECONDS", "25"))
        self.output_dir = Path(os.getenv("OUTPUT_DIR", "outputs"))


settings = Settings()
