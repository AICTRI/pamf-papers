import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import argparse
import csv
import itertools
import json
from collections import Counter
from pathlib import Path

from openpyxl import load_workbook

from _paths import EXPERTS


LABELS = ("Optional", "Recommended", "Mandatory")
EXPERIENCE_RANGES = ("5-9", "10-14", "15-19", "20+")


def read_participant_metadata(path: Path) -> dict[str, str]:
    workbook = load_workbook(path, read_only=True, data_only=True)
    worksheet = workbook["Participant"]
    metadata = {
        str(field or "").strip(): str(response or "").strip()
        for field, response, *_ in worksheet.iter_rows(min_row=2, values_only=True)
        if field
    }
    workbook.close()
    required_nonempty = (
        "Anonymous participant ID",
        "Recruitment channel",
        "Current architecture role",
        "Architecture experience range (5-9 / 10-14 / 15-19 / 20+)",
        "Relevant data/integration/security experience",
        "Completion date",
    )
    missing = [field for field in required_nonempty if not metadata.get(field)]
    if missing:
        raise ValueError(f"Missing participant metadata in {path.name}: {missing}")
    experience = metadata[
        "Architecture experience range (5-9 / 10-14 / 15-19 / 20+)"
    ]
    if experience not in EXPERIENCE_RANGES:
        raise ValueError(f"Invalid experience range in {path.name}: {experience}")
    if metadata["Recruitment channel"] == "WeChat/Weibo":
        if experience == "5-9":
            raise ValueError(f"China-track participant lacks 10 years experience: {path.name}")
        if metadata.get("Multinational/cross-border project experience") != "Yes":
            raise ValueError(
                f"China-track participant lacks multinational project experience: {path.name}"
            )
    expected = {
        "Architecture work in last two years (Yes)": "Yes",
        "Prior AVDM/AXISRobo-PAMP/manuscript exposure (No)": "No",
        "Independent assessment confirmed (Yes)": "Yes",
        "Informed consent confirmed (Yes)": "Yes",
        "No confidential employer/client information included (Yes)": "Yes",
    }
    invalid = {
        field: metadata.get(field)
        for field, expected_value in expected.items()
        if metadata.get(field) != expected_value
    }
    if invalid:
        raise ValueError(f"Eligibility/consent check failed in {path.name}: {invalid}")
    return metadata


def read_ratings(path: Path, rating_column: str) -> dict[str, str]:
    if path.suffix.lower() == ".xlsx":
        workbook = load_workbook(path, read_only=True, data_only=True)
        worksheet = workbook["Ratings"]
        rows = list(worksheet.iter_rows(values_only=True))
        headers = [str(value or "").strip() for value in rows[0]]
        item_index = headers.index("item_id")
        rating_index = headers.index(rating_column)
        ratings = {
            str(row[item_index] or "").strip(): str(row[rating_index] or "").strip()
            for row in rows[1:]
            if row[item_index]
        }
        workbook.close()
    else:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            rows = list(csv.DictReader(handle))
        ratings = {row["item_id"].strip(): row[rating_column].strip() for row in rows}
    invalid = {key: value for key, value in ratings.items() if value not in LABELS}
    if invalid:
        raise ValueError(f"Invalid or blank ratings in {path.name}: {invalid}")
    return ratings


def fleiss_kappa(raters: list[dict[str, str]], item_ids: list[str]) -> float:
    n_raters = len(raters)
    category_totals = Counter()
    item_agreements = []
    for item_id in item_ids:
        counts = Counter(rater[item_id] for rater in raters)
        category_totals.update(counts)
        item_agreements.append(
            sum(count * (count - 1) for count in counts.values())
            / (n_raters * (n_raters - 1))
        )
    observed = sum(item_agreements) / len(item_agreements)
    total_ratings = len(item_ids) * n_raters
    expected = sum((category_totals[label] / total_ratings) ** 2 for label in LABELS)
    return (observed - expected) / (1 - expected) if expected < 1 else 1.0


def exact_agreement(left: dict[str, str], right: dict[str, str], item_ids: list[str]) -> float:
    return sum(left[key] == right[key] for key in item_ids) / len(item_ids)


def weighted_kappa(left: dict[str, str], right: dict[str, str], item_ids: list[str]) -> float:
    size = len(LABELS)
    observed = [[0.0] * size for _ in range(size)]
    for item_id in item_ids:
        observed[LABELS.index(left[item_id])][LABELS.index(right[item_id])] += 1
    total = len(item_ids)
    left_marginal = [sum(row) / total for row in observed]
    right_marginal = [sum(observed[i][j] for i in range(size)) / total for j in range(size)]
    observed_disagreement = 0.0
    expected_disagreement = 0.0
    for i in range(size):
        for j in range(size):
            weight = abs(i - j) / (size - 1)
            observed_disagreement += weight * observed[i][j] / total
            expected_disagreement += weight * left_marginal[i] * right_marginal[j]
    return 1 - observed_disagreement / expected_disagreement if expected_disagreement else 1.0


def majority_rating(raters: list[dict[str, str]], item_id: str) -> str:
    counts = Counter(rater[item_id] for rater in raters)
    highest = max(counts.values())
    winners = [label for label in LABELS if counts[label] == highest]
    return winners[-1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--study-dir", type=Path, default=EXPERTS
    )
    args = parser.parse_args()

    rating_files = sorted((args.study_dir / "ratings").glob("*.xlsx"))
    if len(rating_files) < 3:
        raise ValueError("At least three completed expert rating files are required")
    if len(rating_files) % 2 == 0:
        raise ValueError("Use an odd number of experts so majority labels cannot tie")
    reference = read_ratings(args.study_dir / "avdm_reference_private.csv", "avdm_rating")
    item_ids = sorted(reference)
    experts = [read_ratings(path, "rating") for path in rating_files]
    participant_metadata = [read_participant_metadata(path) for path in rating_files]
    for path, expert in zip(rating_files, experts):
        if set(expert) != set(item_ids):
            raise ValueError(f"Item set differs in {path.name}")

    pairwise = []
    for (left_path, left), (right_path, right) in itertools.combinations(
        zip(rating_files, experts), 2
    ):
        pairwise.append(
            {
                "left": left_path.stem,
                "right": right_path.stem,
                "exact_agreement": exact_agreement(left, right, item_ids),
                "weighted_kappa": weighted_kappa(left, right, item_ids),
            }
        )
    expert_avdm = [
        {
            "expert": path.stem,
            "exact_agreement": exact_agreement(expert, reference, item_ids),
            "weighted_kappa": weighted_kappa(expert, reference, item_ids),
        }
        for path, expert in zip(rating_files, experts)
    ]
    consensus = {item_id: majority_rating(experts, item_id) for item_id in item_ids}
    disagreements = [
        {
            "item_id": item_id,
            "avdm": reference[item_id],
            "expert_majority": consensus[item_id],
            "expert_ratings": [expert[item_id] for expert in experts],
        }
        for item_id in item_ids
        if consensus[item_id] != reference[item_id]
    ]
    result = {
        "expert_count": len(experts),
        "participant_metadata": participant_metadata,
        "item_count": len(item_ids),
        "fleiss_kappa": fleiss_kappa(experts, item_ids),
        "pairwise": pairwise,
        "expert_vs_avdm": expert_avdm,
        "majority_vs_avdm": {
            "exact_agreement": exact_agreement(consensus, reference, item_ids),
            "weighted_kappa": weighted_kappa(consensus, reference, item_ids),
        },
        "disagreements": disagreements,
    }
    output = args.study_dir / "agreement_results.json"
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
