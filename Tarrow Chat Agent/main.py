"""Command-line entry point for Tarrow Chat Agent."""

from __future__ import annotations

import argparse

from helpers.tarot_engine import DEFAULT_BASE_URL, DEFAULT_MODEL, run_reading


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Run an advanced Tarrow Chat Agent reading from the terminal.")
    parser.add_argument("question", nargs="*", help="Question or context for the tarot reading.")
    parser.add_argument("--cards", type=int, default=3, choices=[3, 5, 7], help="Number of cards to draw.")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Ollama model name.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="Ollama base URL.")
    return parser.parse_args()


def main() -> None:
    """Run the terminal workflow."""
    args = parse_args()
    question = " ".join(args.question).strip() or input("Enter your question or context: ").strip()
    result = run_reading(question=question, num_cards=args.cards, model=args.model, base_url=args.base_url)

    print("\nTarrow Chat Agent")
    print("=" * 20)
    print("\nCards drawn:")
    for index, card in enumerate(result.get("cards", []), start=1):
        print(f"{index}. {card.name} ({card.orientation})")

    if result.get("error"):
        print("\nNote: Ollama was not reachable. A local fallback reading was generated.")

    print("\nReading:\n")
    print(result.get("response", "No reading was generated."))


if __name__ == "__main__":
    main()
