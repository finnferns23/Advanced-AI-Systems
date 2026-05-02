from __future__ import annotations

import argparse

from config import settings
from schemas import GameBrief
from tools.report_builder import save_outputs
from tools.validators import validate_package
from workflows.orchestrator import GameDesignOrchestrator


def build_brief_from_args() -> GameBrief:
    parser = argparse.ArgumentParser(description="Run the Game Design Agent Team")
    parser.add_argument("--title", default="Echoes of Ember")
    parser.add_argument("--genre", default="Action Adventure")
    parser.add_argument("--audience", default="Indie PC and console players")
    parser.add_argument("--platform", default="PC")
    parser.add_argument("--theme", default="Memory, survival, and discovery")
    parser.add_argument("--constraints", default="Prototype-first, accessible, realistic indie scope")
    parser.add_argument("--target-rating", default="Teen")
    parser.add_argument("--monetization", default="Premium indie release")
    args = parser.parse_args()
    return GameBrief(args.title, args.genre, args.audience, args.platform, args.theme, args.constraints, args.target_rating, args.monetization)


def run_pipeline(brief: GameBrief):
    package = GameDesignOrchestrator().run(brief)
    issues = validate_package(package)
    if issues:
        raise ValueError("Validation failed: " + "; ".join(issues))
    paths = save_outputs(package, settings.output_dir)
    return package, paths


def main() -> None:
    brief = build_brief_from_args()
    package, paths = run_pipeline(brief)
    print(package.combined_summary)
    print(f"Report saved to: {paths['report']}")
    print(f"JSON saved to: {paths['json']}")


if __name__ == "__main__":
    main()
