import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import argparse
import csv
import json
import math
from collections import Counter
from pathlib import Path

from _paths import PUBLIC, RESULTS


CLASSIFICATIONS = ("Mandatory", "Recommended", "Optional")


def concern_score(raw_score: float, complexity: float, weight_scale: float = 1.0) -> float:
    # Continuous, floor-zero scoring on the 0-5 contribution scale: unactivated
    # concerns score exactly 0.0; activated ones score
    # min(5, raw * scale) / 5 plus the complexity boost. The optional scale
    # multiplies an already aggregated activation, not an individual mapping.
    if raw_score <= 0:
        return 0.0
    base = min(5.0, raw_score * weight_scale) / 5.0
    return min(1.0, round(base + 0.15 * complexity, 4))


def classify(score: float, mandatory: float, recommended: float) -> str:
    if score >= mandatory:
        return "Mandatory"
    if score >= recommended:
        return "Recommended"
    return "Optional"


def raw_scores(fixture: dict) -> dict[str, float]:
    return {
        item["concern_key"]: float(item["raw_activation_score"])
        for item in fixture["risk_items"]
    }


def distribution(
    concern_keys: list[str],
    scores: dict[str, float],
    complexity: float,
    mandatory: float,
    recommended: float,
    weight_scale: float = 1.0,
) -> Counter:
    return Counter(
        classify(
            concern_score(scores.get(key, 0.0), complexity, weight_scale),
            mandatory,
            recommended,
        )
        for key in concern_keys
    )


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--fixture",
        type=Path,
        default=PUBLIC / "case_x_fixture.json",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=RESULTS
    )
    args = parser.parse_args()

    fixture = json.loads(args.fixture.read_text(encoding="utf-8"))
    complexity = float(fixture["project_complexity"])
    scores = raw_scores(fixture)
    concern_keys = [
        decision["concern_key"] for decision in fixture["decisions"]
    ]
    stored = {
        decision["concern_key"]: decision["classification"]
        for decision in fixture["decisions"]
    }
    reproduced = {
        key: classify(concern_score(scores.get(key, 0.0), complexity), 0.90, 0.50)
        for key in concern_keys
    }
    mismatches = {
        key: {"stored": stored[key], "reproduced": reproduced[key]}
        for key in concern_keys
        if stored[key] != reproduced[key]
    }
    if mismatches:
        raise ValueError(f"Baseline reproduction failed: {mismatches}")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    threshold_rows = []
    for mandatory in (0.80, 0.85, 0.88, 0.90, 0.92, 0.95):
        for recommended in (0.40, 0.45, 0.50, 0.55, 0.60):
            if recommended >= mandatory:
                continue
            counts = distribution(
                concern_keys, scores, complexity, mandatory, recommended
            )
            threshold_rows.append(
                {
                    "mandatory_threshold": mandatory,
                    "recommended_threshold": recommended,
                    **{name: counts[name] for name in CLASSIFICATIONS},
                }
            )
    write_csv(
        args.output_dir / "threshold_sensitivity.csv",
        ["mandatory_threshold", "recommended_threshold", *CLASSIFICATIONS],
        threshold_rows,
    )

    weight_rows = []
    for scale in (0.8, 0.9, 1.0, 1.1, 1.2):
        counts = distribution(concern_keys, scores, complexity, 0.90, 0.50, scale)
        weight_rows.append(
            {
                "weight_scale": scale,
                **{name: counts[name] for name in CLASSIFICATIONS},
            }
        )
    write_csv(
        args.output_dir / "weight_sensitivity.csv",
        ["weight_scale", *CLASSIFICATIONS],
        weight_rows,
    )

    ablated_scores = dict(scores)
    for key in ("D7", "D9", "SCR7", "SCR1"):
        ablated_scores[key] = max(0.0, ablated_scores.get(key, 0.0) - 2.0)
    baseline = distribution(concern_keys, scores, complexity, 0.90, 0.50)
    ablated = distribution(concern_keys, ablated_scores, complexity, 0.90, 0.50)
    ablation_rows = [
        {"condition": "aggregate_scores_reference", **baseline},
        {"condition": "four_scores_reduced_by_2p0", **ablated},
    ]
    write_csv(
        args.output_dir / "combination_rule_ablation.csv",
        ["condition", *CLASSIFICATIONS],
        ablation_rows,
    )

    report = [
        "# Cross-Border Case Sensitivity Analysis",
        "",
        "Source: public constructed benchmark fixture `case-x`.",
        f"Project complexity: `{complexity:.3f}`; concerns classified: `{len(concern_keys)}`.",
        "",
        "## Baseline",
        "",
        f"Mandatory: {baseline['Mandatory']}; Recommended: {baseline['Recommended']}; Optional: {baseline['Optional']}.",
        "",
        "## Uniform Aggregated-Activation Perturbation",
        "",
        "The multiplier is applied to frozen per-concern aggregated activation totals, not to individual mapping or rule weights; this test does not rerun max-plus-bonus aggregation.",
        "",
        "| Weight multiplier | Mandatory | Recommended | Optional |",
        "|---:|---:|---:|---:|",
    ]
    report.extend(
        f"| {row['weight_scale']:.1f} | {row['Mandatory']} | {row['Recommended']} | {row['Optional']} |"
        for row in weight_rows
    )
    report.extend(
        [
            "",
            "## Cross-Border Aggregate-Score Stress Test",
            "",
            "| Condition | Mandatory | Recommended | Optional |",
            "|---|---:|---:|---:|",
        ]
    )
    report.extend(
        f"| {row['condition']} | {row['Mandatory']} | {row['Recommended']} | {row['Optional']} |"
        for row in ablation_rows
    )
    report.extend(
        [
            "",
            "Threshold-grid results are in `threshold_sensitivity.csv`.",
            "The four selected aggregate scores are reduced by 2.0 as a transparent counterfactual stress test; this is not a replay of the underlying rule engine.",
            "The analysis evaluates robustness of frozen aggregate classifications, not raw mapping weights or external correctness.",
        ]
    )
    (args.output_dir / "sensitivity_report.md").write_text(
        "\n".join(report) + "\n", encoding="utf-8"
    )
    print(args.output_dir / "sensitivity_report.md")


if __name__ == "__main__":
    main()
