import argparse
import csv
import json
import math
from collections import Counter
from pathlib import Path


CLASSIFICATIONS = ("Mandatory", "Recommended", "Optional")


def risk_levels(raw_score: float) -> tuple[int, int]:
    bounded = min(25.0, max(1.0, raw_score))
    severity = min(5, max(1, math.ceil(math.sqrt(bounded))))
    likelihood = min(5, max(1, math.ceil(bounded / severity)))
    return severity, likelihood


def concern_score(raw_score: float, complexity: float, weight_scale: float = 1.0) -> float:
    if raw_score <= 0:
        base = 0.0
    else:
        severity, likelihood = risk_levels(raw_score * weight_scale)
        base = (severity / 5.0) * (likelihood / 5.0)
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
        default=Path(__file__).parent / "public" / "case_x_fixture.json",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=Path(__file__).parent / "results"
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
        key: classify(concern_score(scores.get(key, 0.0), complexity), 0.66, 0.38)
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
    for mandatory in (0.60, 0.63, 0.66, 0.70, 0.73, 0.75):
        for recommended in (0.30, 0.34, 0.38, 0.42, 0.46):
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
        counts = distribution(concern_keys, scores, complexity, 0.66, 0.38, scale)
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
        ablated_scores[key] = max(0.0, ablated_scores.get(key, 0.0) - 15.0)
    baseline = distribution(concern_keys, scores, complexity, 0.66, 0.38)
    ablated = distribution(concern_keys, ablated_scores, complexity, 0.66, 0.38)
    ablation_rows = [
        {"condition": "combination_rule_enabled", **baseline},
        {"condition": "combination_rule_ablated", **ablated},
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
        "## Uniform Weight Perturbation",
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
            "## Cross-Border Combination-Rule Ablation",
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
            "The analysis evaluates robustness of classifications, not their external correctness.",
        ]
    )
    (args.output_dir / "sensitivity_report.md").write_text(
        "\n".join(report) + "\n", encoding="utf-8"
    )
    print(args.output_dir / "sensitivity_report.md")


if __name__ == "__main__":
    main()
