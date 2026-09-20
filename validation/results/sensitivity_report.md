# Cross-Border Case Sensitivity Analysis

Source: public constructed benchmark fixture `case-x`.
Project complexity: `0.500`; concerns classified: `61`.

## Baseline

Mandatory: 32; Recommended: 14; Optional: 15.

## Uniform Aggregated-Activation Perturbation

The multiplier is applied to frozen per-concern aggregated activation totals, not to individual mapping or rule weights; this test does not rerun max-plus-bonus aggregation.

| Weight multiplier | Mandatory | Recommended | Optional |
|---:|---:|---:|---:|
| 0.8 | 0 | 46 | 15 |
| 0.9 | 27 | 19 | 15 |
| 1.0 | 32 | 14 | 15 |
| 1.1 | 38 | 8 | 15 |
| 1.2 | 38 | 8 | 15 |

## Cross-Border Aggregate-Score Stress Test

| Condition | Mandatory | Recommended | Optional |
|---|---:|---:|---:|
| aggregate_scores_reference | 32 | 14 | 15 |
| four_scores_reduced_by_2p0 | 28 | 18 | 15 |

Threshold-grid results are in `threshold_sensitivity.csv`.
The four selected aggregate scores are reduced by 2.0 as a transparent counterfactual stress test; this is not a replay of the underlying rule engine.
The analysis evaluates robustness of frozen aggregate classifications, not raw mapping weights or external correctness.
