# AVDM R3 Validation Materials (Public Subset)

Reproducible validation materials for the R3 revision of the AVDM manuscript.
All cases are constructed, fictional benchmarks and do not represent any actual
company, client, employee, or project.

## Layout

| Path | Description |
|------|-------------|
| `public/` | Sanitized fixtures and the release manifest |
| `results/` | Aggregate sensitivity and contrast results |
| `expert-study/` | Blind comparison protocol, case brief, blank rating form, recruitment templates |
| `expert-study-cn/` | China-track case brief and aggregate round-2 agreement results |
| `survey-forms/` | Questionnaire item bank and platform import templates |

## Run

```sh
python run_sensitivity.py
python test_analysis.py
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
