# PAMF Papers

Public research artifacts for the AVDM (Architecture Viewpoint Decision Model)
work, including the validation materials for the R3 revision.

This repository intentionally contains **only release-approved validation
materials**. Manuscript sources, reviewer correspondence, participant-level
data, and recruitment records remain private. See [`PRIVACY.md`](PRIVACY.md)
for the boundary.

## Contents

| Path | Description |
|------|-------------|
| `public/` | Fictional benchmark fixtures (`case_x`, `case_m`, `case_low_risk`) with SHA-256 digests and the release manifest |
| `validation/expert-study/` | Blind expert comparison protocol, case brief, rating form, and recruitment templates |
| `validation/expert-study-cn/` | China-track case brief and aggregate round-2 agreement results |
| `validation/results/` | Aggregate sensitivity, threshold, and combination-rule results |
| `validation/survey-forms/` | Questionnaire item bank and platform import templates |
| `scripts/analysis/` | Reproducible sensitivity and agreement analysis scripts |

## Reproduce the analysis

Run from the repository root:

```sh
pip install openpyxl
python scripts/analysis/run_sensitivity.py
python scripts/analysis/test_analysis.py
```

The expert-rating analysis (`scripts/analysis/analyze_expert_ratings.py`)
requires frozen participant workbooks that are not distributed publicly.

## Related software

The open-source implementation is maintained at
<https://github.com/axisrobo/AXISRobo-PAMP>.

## License

Code is released under the MIT License (`LICENSE`). Documentation, fixtures,
and aggregate results are released under CC BY 4.0 unless stated otherwise.
