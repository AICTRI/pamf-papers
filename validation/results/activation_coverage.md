# Activation Coverage Diagnostic

AVDM scores every concern, but only concerns activated by questionnaire
answers or concern-mapping rules receive a non-zero activation. A concern
with no activation receives score zero and therefore always classifies as Optional.

Consequently, Mandatory/Recommended outcomes can only appear among
activated concerns. Unactivated Optional concerns reflect missing input
coverage, not a case-specific judgement that the viewpoint is low value.
This is the input-representation gap that makes expert-versus-AVDM
agreement descriptive rather than a controlled comparison.

| Fixture | Concerns | Activated | Coverage | M/R/O (activated) | M/R/O (unactivated) |
|---|---:|---:|---:|---|---|
| case_low_risk_fixture | 61 | 5 | 0.08 | 0/4/1 | 0/0/56 |
| case_m_fixture | 61 | 17 | 0.28 | 5/10/2 | 0/0/44 |
| case_x_fixture | 61 | 46 | 0.75 | 32/14/0 | 0/0/15 |

Per-concern unactivated keys are listed in `activation_coverage.csv`.
