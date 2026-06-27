from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    app_name: str = "Atlas AI Intelligent Studio"
    app_tagline: str = "Production-focused AI workspace for assistants, knowledge, vision, voice, and MCP planning."
    data_dir: Path = Path("data")
    openai_api_key: str | None = None
    model: str = "gpt-4.1-mini"
    audio_model: str = "gpt-4o-mini-tts"
    voice: str = "nova"
    chunk_size: int = 1000
    overlap: int = 150

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            data_dir=Path(os.getenv("ATLAS_DATA_DIR", "data")),
            openai_api_key=os.getenv("OPENAI_API_KEY") or None,
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            audio_model=os.getenv("OPENAI_TTS_MODEL", "gpt-4o-mini-tts"),
            voice=os.getenv("OPENAI_TTS_VOICE", "nova"),
            chunk_size=_env_int("ATLAS_CHUNK_SIZE", 1000),
            overlap=_env_int("ATLAS_CHUNK_OVERLAP", 150),
        )


def _env_int(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        return default
    try:
        return int(raw)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer.") from exc


def choose_secret(user_value: str | None, env_value: str | None) -> str | None:
    user_value = (user_value or "").strip()
    env_value = (env_value or "").strip()
    return user_value or env_value or None
