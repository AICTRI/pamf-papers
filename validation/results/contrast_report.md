# Contrast Analysis: Saturated vs Low-Risk Scenario

## Scenario summary at reference configuration (0.90 / 0.50)

| Scenario | Complexity | Mandatory | Recommended | Optional | Mandatory share |
|---|---:|---:|---:|---:|---:|
| Case X (high risk) | 0.50 | 32 | 14 | 15 | 52.5% |
| Case M (moderate risk) | 0.40 | 5 | 10 | 46 | 8.2% |
| Case L (lower-bound check) | 0.20 | 0 | 4 | 57 | 0.0% |

## Expert agreement on the saturated scenario

- Fleiss' kappa among experts: -0.036
- Expert-majority vs AVDM exact agreement: 0.541
- Expert-majority vs AVDM weighted kappa: 0.062
- Expert-majority Mandatory count: 56 of 61

The saturated scenario activates every major risk dimension, so expert
ratings concentrate in Mandatory and provide little discrimination. AVDM
remains parameterised and can be moved along its threshold curve; the
low-risk contrast scenario shows that the same mechanism collapses to
almost no Mandatory viewpoints when the risk signals are absent.

## Threshold behaviour

`threshold_contrast.csv` reports both scenarios across mandatory
thresholds from 0.80 to 0.95. As the threshold rises, AVDM can be forced
to emit fewer Mandatory viewpoints, but the Recommended band disappears,
so a single global threshold cannot reproduce an expert-style all-Mandatory
partition. This is the concrete configuration limitation, and it is a
governance choice rather than a defect that can be fitted away.
