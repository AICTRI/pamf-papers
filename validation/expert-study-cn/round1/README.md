# Round 1: Unbounded Expert Ratings

Three enterprise architects rated all 61 Case X viewpoints as Mandatory,
Recommended, or Optional with no budget. Agreement was near chance
(Fleiss' kappa = -0.036; pairwise exact agreement 0.52-0.72) and the majority
marked 56 of 61 viewpoints Mandatory. This motivated the forced-budget
Round 2.

## Published files

| Path | Content |
|---|---|
| `round1_agreement.json` | Aggregate agreement statistics: Fleiss' kappa, pairwise agreement, expert-vs-AVDM and majority-vs-AVDM statistics, majority distribution, and per-item majority labels |
| `case_brief_cn.md` | Case X narrative given to participants |

## Withheld

Participant metadata (role, experience range, recruitment channel, completion
date) and per-item individual expert ratings stay in the private research
workspace. The public file is produced by
`scripts/analysis/export_public_agreement.py`, which drops those fields from the
private `agreement_results.json`.

## Reproducibility note

This file is a frozen aggregate. It is not reproducible from the released
inputs alone because the participant workbooks are private by design.
