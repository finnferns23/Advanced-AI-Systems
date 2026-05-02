from __future__ import annotations

from agents.base_agent import BaseGameAgent
from schemas import AgentResult, GameBrief


class ImageAgent(BaseGameAgent):
    name = "Image Agent"
    role = "Builds art direction, visual bible, asset list, and image-generation prompts"

    def run(self, brief: GameBrief, context: dict | None = None) -> AgentResult:

        style = f"Readable stylized game art matching {brief.theme}; strong silhouettes; accessible contrast."
        outputs = {
            "art_style": style,
            "visual_bible": ["Consistent shape language", "Readable foreground/background separation", "Limited UI icon ambiguity", "Color is never the only signal"],
            "image_prompts": [
                f"Key art for {brief.title}, {brief.genre}, {brief.theme}, cinematic game concept art, readable composition",
                f"Main character sheet for {brief.title}, strong silhouette, production concept art",
                f"Environment concept for {brief.title}, gameplay-readable level space, mood lighting, accessible contrast",
                f"UI icon set for {brief.title}, clean game interface, high contrast, simple shapes",
            ],
            "asset_list": ["Key art", "Character silhouettes", "Environment thumbnails", "UI icons", "Marketing capsule", "Prototype placeholders"],
        }
        return self.result("Image pipeline defines visual style, prompts, and production asset requirements.", outputs, ["Generated images may be inconsistent without style-locking"], ["Pick one visual bible before creating final assets"])
