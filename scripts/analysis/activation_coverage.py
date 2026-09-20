import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

from _paths import PUBLIC, RESULTS


CLASSIFICATIONS = ("Mandatory", "Recommended", "Optional")


def analyze(fixture_path: Path) -> dict:
    fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    activated = {item["concern_key"] for item in fixture["risk_items"]}
    decisions = fixture["decisions"]
    total = len(decisions)
    active = [item for item in decisions if item["concern_key"] in activated]
    inactive = [item for item in decisions if item["concern_key"] not in activated]
    active_counts = Counter(item["classification"] for item in active)
    inactive_counts = Counter(item["classification"] for item in inactive)
    return {
        "fixture": fixture_path.stem,
        "scenario_id": fixture.get("scenario_id", ""),
        "project_complexity": fixture.get("project_complexity"),
        "concerns_total": total,
        "concerns_activated": len(activated),
        "concerns_unactivated": total - len(activated),
        "coverage_ratio": round(len(activated) / total, 4) if total else 0.0,
        "activated_Mandatory": active_counts["Mandatory"],
        "activated_Recommended": active_counts["Recommended"],
        "activated_Optional": active_counts["Optional"],
        "unactivated_Mandatory": inactive_counts["Mandatory"],
        "unactivated_Recommended": inactive_counts["Recommended"],
        "unactivated_Optional": inactive_counts["Optional"],
        "unactivated_keys": ";".join(
            sorted(item["concern_key"] for item in inactive)
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Report questionnaire activation coverage per public fixture. "
            "Concerns with no activation receive score zero and always classify "
            "as Optional, so Mandatory/Recommended outcomes can "
            "only occur among activated concerns."
        )
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        action="append",
        help="Fixture file(s); defaults to every case_*_fixture.json in PUBLIC.",
    )
    parser.add_argument("--output-dir", type=Path, default=RESULTS)
    args = parser.parse_args()

    fixtures = args.fixture or sorted(PUBLIC.glob("case_*_fixture.json"))
    if not fixtures:
        raise SystemExit(f"No fixtures found under {PUBLIC}")

    rows = [analyze(path) for path in fixtures]

    leaks = [
        row
        for row in rows
        if row["unactivated_Mandatory"] or row["unactivated_Recommended"]
    ]
    if leaks:
        for row in leaks:
            print(
                "WARNING: unactivated concerns classified above Optional in "
                f"{row['fixture']} (M={row['unactivated_Mandatory']}, "
                f"R={row['unactivated_Recommended']})"
            )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    fields = [
        "fixture",
        "scenario_id",
        "project_complexity",
        "concerns_total",
        "concerns_activated",
        "concerns_unactivated",
        "coverage_ratio",
        "activated_Mandatory",
        "activated_Recommended",
        "activated_Optional",
        "unactivated_Mandatory",
        "unactivated_Recommended",
        "unactivated_Optional",
        "unactivated_keys",
    ]
    with (args.output_dir / "activation_coverage.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    report = [
        "# Activation Coverage Diagnostic",
        "",
        "AVDM scores every concern, but only concerns activated by questionnaire",
        "answers or concern-mapping rules receive a non-zero activation. A concern",
        "with no activation receives score zero and therefore always classifies as Optional.",
        "",
        "Consequently, Mandatory/Recommended outcomes can only appear among",
        "activated concerns. Unactivated Optional concerns reflect missing input",
        "coverage, not a case-specific judgement that the viewpoint is low value.",
        "This is the input-representation gap that makes expert-versus-AVDM",
        "agreement descriptive rather than a controlled comparison.",
        "",
        "| Fixture | Concerns | Activated | Coverage | M/R/O (activated) | M/R/O (unactivated) |",
        "|---|---:|---:|---:|---|---|",
    ]
    report.extend(
        f"| {row['fixture']} | {row['concerns_total']} | "
        f"{row['concerns_activated']} | {row['coverage_ratio']:.2f} | "
        f"{row['activated_Mandatory']}/{row['activated_Recommended']}/"
        f"{row['activated_Optional']} | "
        f"{row['unactivated_Mandatory']}/{row['unactivated_Recommended']}/"
        f"{row['unactivated_Optional']} |"
        for row in rows
    )
    report.extend(
        [
            "",
            "Per-concern unactivated keys are listed in `activation_coverage.csv`.",
        ]
    )
    (args.output_dir / "activation_coverage.md").write_text(
        "\n".join(report) + "\n", encoding="utf-8"
    )
    print(args.output_dir / "activation_coverage.csv")
    print(args.output_dir / "activation_coverage.md")


if __name__ == "__main__":
    main()
