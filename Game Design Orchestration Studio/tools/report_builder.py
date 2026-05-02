from __future__ import annotations

import json
from pathlib import Path

from schemas import DesignPackage


def build_markdown_report(package: DesignPackage) -> str:
    lines = [
        f"# {package.brief.title} - Game Design Package",
        "",
        "## Brief",
        f"- Genre: {package.brief.genre}",
        f"- Audience: {package.brief.audience}",
        f"- Platform: {package.brief.platform}",
        f"- Theme: {package.brief.theme}",
        f"- Constraints: {package.brief.constraints}",
        f"- Target Rating: {package.brief.target_rating}",
        f"- Monetization: {package.brief.monetization}",
        "",
        "## Combined Summary",
        package.combined_summary,
        "",
        "## Agent Outputs",
    ]
    for result in package.results:
        lines.extend([
            "",
            f"### {result.agent_name}",
            f"**Role:** {result.role}",
            "",
            result.summary,
            "",
            "**Outputs**",
            "```json",
            json.dumps(result.outputs, indent=2, ensure_ascii=False),
            "```",
        ])
        if result.risks:
            lines.extend(["", "**Risks**"] + [f"- {item}" for item in result.risks])
        if result.next_steps:
            lines.extend(["", "**Next Steps**"] + [f"- {item}" for item in result.next_steps])
    lines.extend([
        "",
        "## Production Plan",
        "```json",
        json.dumps(package.production_plan, indent=2, ensure_ascii=False),
        "```",
    ])
    return "\n".join(lines).strip() + "\n"


def save_outputs(package: DesignPackage, output_dir: str | Path) -> dict[str, Path]:
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    report_path = path / "game_design_report.md"
    json_path = path / "game_design_package.json"
    report_path.write_text(build_markdown_report(package), encoding="utf-8")
    json_path.write_text(json.dumps(package.to_dict(), indent=2, ensure_ascii=False), encoding="utf-8")
    return {"report": report_path, "json": json_path}
