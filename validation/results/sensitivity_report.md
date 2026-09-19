# Cross-Border Case Sensitivity Analysis

Source: public constructed benchmark fixture `case-x`.
Project complexity: `0.500`; concerns classified: `61`.

## Baseline

Mandatory: 13; Recommended: 10; Optional: 38.

## Uniform Weight Perturbation

| Weight multiplier | Mandatory | Recommended | Optional |
|---:|---:|---:|---:|
| 0.8 | 12 | 11 | 38 |
| 0.9 | 13 | 10 | 38 |
| 1.0 | 13 | 10 | 38 |
| 1.1 | 13 | 10 | 38 |
| 1.2 | 13 | 10 | 38 |

## Cross-Border Combination-Rule Ablation

| Condition | Mandatory | Recommended | Optional |
|---|---:|---:|---:|
| combination_rule_enabled | 13 | 10 | 38 |
| combination_rule_ablated | 9 | 13 | 39 |

Threshold-grid results are in `threshold_sensitivity.csv`.
The analysis evaluates robustness of classifications, not their external correctness.
