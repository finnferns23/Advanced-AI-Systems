"""Session memory utilities."""

from __future__ import annotations

from core.models import SessionMemory


_GLOBAL_MEMORY = SessionMemory()


def get_memory() -> SessionMemory:
    """Return process-level memory for CLI use."""
    return _GLOBAL_MEMORY
