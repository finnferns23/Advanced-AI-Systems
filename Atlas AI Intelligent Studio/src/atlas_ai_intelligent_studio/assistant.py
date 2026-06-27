from __future__ import annotations

import base64
from pathlib import Path
from uuid import uuid4

from openai import OpenAI

from .rag import DocumentChunk


class AtlasAssistant:
    """OpenAI-backed service layer for Atlas AI Intelligent Studio.

    The client is initialized only when an API key is present, so the dashboard,
    local checks, and tests can run safely without secrets.
    """

    def __init__(self, api_key: str | None, model: str, audio_model: str) -> None:
        if not api_key:
            raise ValueError("OpenAI API key is required for AI generation.")
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.audio_model = audio_model

    def respond(self, instruction: str, context_chunks: list[DocumentChunk] | None = None) -> str:
        context = ""
        if context_chunks:
            context = "\n\n".join(f"Source: {chunk.source}\n{chunk.text}" for chunk in context_chunks)

        prompt = f"""
You are Atlas AI Intelligent Studio, a production-focused AI assistant workspace.

User request:
{instruction}

Available uploaded-document context:
{context or 'No uploaded document context was provided.'}

Operating rules:
- Use uploaded context when it is relevant.
- State clearly when provided context is insufficient.
- Do not invent files, sources, browsing results, execution results, prices, schedules, credentials, or tool outputs.
- Keep responses practical, concise, professional, and implementation-focused.
- For plans, include assumptions, risks, and validation checks.
""".strip()

        response = self.client.responses.create(
            model=self.model,
            input=prompt,
            temperature=0.3,
        )
        return response.output_text.strip()

    def analyze_image(self, image_bytes: bytes, mime_type: str, question: str) -> str:
        encoded = base64.b64encode(image_bytes).decode("ascii")
        response = self.client.responses.create(
            model=self.model,
            input=[
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": question},
                        {"type": "input_image", "image_url": f"data:{mime_type};base64,{encoded}"},
                    ],
                }
            ],
            temperature=0.2,
        )
        return response.output_text.strip()

    def create_audio(self, text: str, output_dir: Path, voice: str) -> Path:
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"atlas_voice_{uuid4().hex[:10]}.mp3"
        with self.client.audio.speech.with_streaming_response.create(
            model=self.audio_model,
            voice=voice,
            input=text,
        ) as response:
            response.stream_to_file(output_path)
        return output_path
