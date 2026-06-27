from __future__ import annotations

import hashlib
import math
from dataclasses import dataclass
from uuid import uuid4

from .text import chunk_text


@dataclass(frozen=True)
class DocumentChunk:
    id: str
    source: str
    text: str
    vector: dict[str, float]


def _token_vector(text: str, dimensions: int = 2048) -> dict[str, float]:
    vector: dict[str, float] = {}
    for raw in text.lower().split():
        token = raw.strip(".,;:!?()[]{}<>\\\"'")
        if not token:
            continue
        digest = hashlib.sha256(token.encode("utf-8")).hexdigest()[:8]
        key = str(int(digest, 16) % dimensions)
        vector[key] = vector.get(key, 0.0) + 1.0
    norm = math.sqrt(sum(value * value for value in vector.values())) or 1.0
    return {key: value / norm for key, value in vector.items()}


def _cosine(left: dict[str, float], right: dict[str, float]) -> float:
    if len(left) > len(right):
        left, right = right, left
    return sum(value * right.get(key, 0.0) for key, value in left.items())


class MemoryIndex:
    def __init__(self, chunk_size: int = 1000, overlap: int = 150) -> None:
        if chunk_size <= overlap:
            raise ValueError("chunk_size must be greater than overlap")
        self.chunk_size = chunk_size
        self.overlap = overlap
        self._chunks: list[DocumentChunk] = []

    @property
    def count(self) -> int:
        return len(self._chunks)

    def add_document(self, source: str, text: str) -> int:
        chunks = [
            DocumentChunk(id=uuid4().hex, source=source, text=chunk, vector=_token_vector(chunk))
            for chunk in chunk_text(text, chunk_size=self.chunk_size, overlap=self.overlap)
        ]
        self._chunks.extend(chunks)
        return len(chunks)

    def search(self, query: str, limit: int = 5) -> list[DocumentChunk]:
        query_vector = _token_vector(query)
        ranked = sorted(
            ((_cosine(query_vector, chunk.vector), chunk) for chunk in self._chunks),
            reverse=True,
            key=lambda item: item[0],
        )
        return [chunk for score, chunk in ranked[:limit] if score > 0]
