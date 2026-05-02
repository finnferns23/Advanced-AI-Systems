from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class DesignMemory:
    """Tiny local JSON memory for reusable design references.

    This is intentionally simple and dependency-free. It can later be replaced with
    ChromaDB, Pinecone, FAISS, or LangChain retrievers.
    """

    def __init__(self, path: str | Path = "memory/design_memory.json") -> None:
        self.path = Path(path)

    def load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {"references": []}
        return json.loads(self.path.read_text(encoding="utf-8"))

    def add_reference(self, title: str, note: str) -> None:
        data = self.load()
        data.setdefault("references", []).append({"title": title, "note": note})
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(data, indent=2), encoding="utf-8")
