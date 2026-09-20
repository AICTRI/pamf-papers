# Input Representation and Activation Coverage

Read this before comparing AVDM classifications with expert judgements.

## AVDM's input is a questionnaire, not the case narrative

AVDM is driven by structured questionnaire answers plus concern-mapping and
activation rules. Only concerns touched by a selected answer or an activated
rule produce a risk item. Every other concern receives score zero and therefore
classifies as **Optional by construction**, independent of project complexity.

As a result, `Mandatory` and `Recommended` outcomes can only ever appear among
**activated** concerns.

## Coverage of the released fixtures

| Fixture | Concerns | Activated | Coverage | M/R/O (activated) | M/R/O (unactivated) |
|---|---:|---:|---:|---|---|
| `case_x_fixture` | 61 | 46 | 0.75 | 32/14/0 | 0/0/15 |
| `case_m_fixture` | 61 | 17 | 0.28 | 5/10/2 | 0/0/44 |
| `case_low_risk_fixture` | 61 | 5 | 0.08 | 0/4/1 | 0/0/56 |

The per-concern unactivated keys are in `validation/results/activation_coverage.csv`;
regenerate with `scripts/analysis/activation_coverage.py`.

## Consequence for the expert comparison

Experts received only the short narrative case brief, whereas AVDM received the
structured questionnaire-derived activations. A disagreement on a viewpoint can
therefore come from two causes that are **not separable** in this design:

1. the expert inferred a relevant concern that was never encoded as a
   questionnaire signal (and AVDM assigned zero activation); or
2. AVDM and the expert genuinely disagree about a concern that both considered.

This is the information asymmetry reported in the manuscript. Expert-versus-AVDM
overlap is consequently a **descriptive observation only**, not a controlled
validity comparison. A like-for-like comparison requires either a common input
(experts answer the same questionnaire) or a published, deterministic
`text -> questionnaire` coding protocol.

## Fixtures are frozen

The fixture files and their SHA-256 digests are part of the published
reproducibility package and are not modified to carry this note. The
input-representation caveat is delivered as this sidecar document plus the
generated `activation_coverage` results.
