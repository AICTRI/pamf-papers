# Public Release Manifest

## Release After Expert Ratings Are Frozen

- `public/README.md`
- `public/case_x_fixture.json`
- `public/case_x_fixture.sha256`
- `public/case_m_fixture.json`
- `public/case_m_fixture.sha256`
- `public/case_low_risk_fixture.json`
- `public/case_low_risk_fixture.sha256`
- `run_sensitivity.py`
- `activation_coverage.py`
- `analyze_expert_ratings.py`
- `test_analysis.py`
- `expert-study/case_brief.md`
- `expert-study/protocol.md`
- `expert-study/expert_rating_form_R3.xlsx`
- Recruitment, screening, consent, assignment, and debrief templates except the private tracker
- Aggregate sensitivity, threshold, and contrast results
- `expert-study-cn/round1/round1_agreement.json` (privacy-safe aggregate; participant metadata and per-item individual ratings removed by `export_public_agreement.py`)
- `expert-study-cn/round2/round2_results.json` (frozen aggregate)
- `scripts/analysis/export_public_agreement.py`, which documents the sanitization step
- De-identified per-item labels only when participants separately consent

## Never Release

- `data/private_avdm_snapshot.json` and its digest
- `export_avdm_snapshot.py`
- `make_public_case_fixture.py`, because it identifies the local source record
- `inspect_avdm_data.py`
- `expert-study/avdm_reference_private.csv` before data freeze
- `expert-study/ratings/` without explicit participant release consent
- `expert-study/recruitment/candidate_tracker_private.csv`
- Consent records, LinkedIn URLs, contact details, identity mappings, payment records, or unreviewed free text
- PostgreSQL credentials, local database names, internal project identifiers, usernames, or timestamps

## Repository Preparation

Publish the approved files under a dedicated path such as
`research/avdm-r3-validation/` rather than exposing the ignored `paper/`
workspace. Replace private paths with relative fixture paths, include a license,
and tag the exact code revision cited by the manuscript.
