# AVDM R3 Validation Materials (Public Subset)

Reproducible validation materials for the R3 revision of the AVDM manuscript.
All cases are constructed, fictional benchmarks and do not represent any actual
company, client, employee, or project.

## Layout

The release-approved fixtures live at the repository root under `public/`. The
analysis scripts live under `scripts/analysis/`. This directory holds the study
materials and aggregate results.

| Path | Description |
|------|-------------|
| `expert-study/` | Blind comparison protocol, case brief, blank rating form, recruitment templates |
| `expert-study-cn/` | China-track case brief and aggregate round-2 agreement results |
| `results/` | Aggregate sensitivity and contrast results |
| `survey-forms/` | Questionnaire item bank and platform import templates |

## Run

Run from the repository root:

```sh
python scripts/analysis/run_sensitivity.py
python scripts/analysis/test_analysis.py
python scripts/analysis/activation_coverage.py
```

Verify a fixture before analysis:

```powershell
Get-FileHash public\case_x_fixture.json -Algorithm SHA256
```

The expected digest is in `public/case_x_fixture.sha256`.

## Release boundary

See `public/PUBLIC_RELEASE_MANIFEST.md` and the repository-level
[`PRIVACY.md`](../PRIVACY.md). Participant-level ratings, identity mappings,
consent and payment records, and the private database snapshot are not part of
this public subset.
