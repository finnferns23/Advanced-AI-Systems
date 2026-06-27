from __future__ import annotations

from pathlib import Path


def validate_mcp_config(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, f"MCP config not found: {path}"
    text = path.read_text(encoding="utf-8", errors="replace")
    required_terms = ["mcp", "server"]
    missing = [term for term in required_terms if term not in text.lower()]
    if missing:
        return False, f"MCP config exists but is missing expected terms: {', '.join(missing)}"
    return True, "MCP config looks structurally valid for a local dry check."


def mcp_run_hint(path: Path) -> str:
    return f"mcp-agent run --config {path}"
