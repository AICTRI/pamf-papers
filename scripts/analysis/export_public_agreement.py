"""Export a privacy-safe Round 1 agreement summary for public release.

The private study directory contains participant metadata and per-item
individual ratings. This script keeps only aggregate statistics and the
majority label per item, so the public package mirrors the private layout
without exposing participant-level data.

Usage:
    python scripts/analysis/export_public_agreement.py <private agreement_results.json> [--output PATH]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

DEFAULT_OUTPUT = (
    Path(__file__).resolve().parents[2]
    / "validation"
    / "expert-study-cn"
    / "round1"
    / "round1_agreement.json"
)

DROP_TOP_LEVEL = ("participant_metadata",)
DROP_ITEM_KEYS = ("expert_ratings",)


def sanitize(result: dict) -> dict:
    public = {key: value for key, value in result.items() if key not in DROP_TOP_LEVEL}
    public["disagreements"] = [
        {key: value for key, value in item.items() if key not in DROP_ITEM_KEYS}
        for item in result.get("disagreements", [])
    ]
    public["release_note"] = (
        "Aggregate statistics only. Participant metadata and per-item individual "
        "ratings are withheld to protect participant privacy."
    )
    return public


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Private agreement_results.json")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    result = json.loads(args.source.read_text(encoding="utf-8"))
    public = sanitize(result)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(public, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(args.output)


if __name__ == "__main__":
    main()
