# AVDM Reference Configuration (R.3.0)

A reader-friendly snapshot of the AVDM decision configuration, so the model can
be understood without installing AXISRobo-PAMP. It is the input side of AVDM:
the questionnaire items, the concern vocabulary, the 0-5 mapping contributions,
the interaction rules, and the classification policy. The benchmark fixtures in
`../` are the output side.

## Files

| File | Content |
|---|---|
| `avdm_concern_catalog.csv` | 68 concerns: key, name, layer, definition, active flag, risk tags |
| `avdm_question_catalog.csv` | 69 questions: id, text, category, answer type, option set, source scope |
| `avdm_question_concern_mapping.csv` | 682 question-answer → concern contributions on the 0-5 scale |
| `avdm_activation_rules.json` | 34 ALL/ANY interaction rules, their 0-5 contributions, and the graded option items |
| `avdm_classification_policy.json` | Thresholds and complexity coefficient used for the reported results |

Each file has a matching `.sha256` with the digest of its exact bytes.

## How it maps to the AVDM decision chain

1. A questionnaire answer selects a question-answer pair.
2. Each pair activates concerns with a 0-5 contribution
   (`avdm_question_concern_mapping.csv`).
3. Convergent contributions for one concern combine as
   `min(5, max(contributions) + 0.25 * (n - 1))`.
4. Interaction rules contribute an additional 0-5 value when their ALL/ANY
   predicate holds (`avdm_activation_rules.json`).
5. The aggregated activation `A` in `[0,5]` and normalised project complexity
   `C` in `[0,1]` give `score = min(1, A/5 + 0.15 * C)`.
6. `score >= 0.90` is Mandatory, `0.50 <= score < 0.90` is Recommended, and
   anything lower (including unactivated concerns, which score exactly 0) is
   Optional (`avdm_classification_policy.json`).

## Provenance and scope

- Exported from the author's AVDM database at the revision tagged `R.3.0` of
  [AXISRobo-PAMP](https://github.com/axisrobo/AXISRobo-PAMP/tree/R.3.0).
- This is a **frozen reference snapshot**. It is not reproducible from the
  released inputs alone, because the source configuration lives in a private
  database; the software repository remains the canonical, editable source.
- The thresholds and the complexity coefficient are **governance policy
  defaults**, not fitted probabilities. An adopting organisation is expected to
  version and recalibrate them.
- No participant data, credentials, or private project identifiers are present.

## Verify

```powershell
Get-ChildItem *.sha256 | ForEach-Object {
  $expected = (Get-Content $_).Split()[0]
  $target = $_.Name -replace '\.sha256$', ''
  $actual = (Get-FileHash $target -Algorithm SHA256).Hash.ToLower()
  "{0}: {1}" -f $target, ($actual -eq $expected)
}
```
