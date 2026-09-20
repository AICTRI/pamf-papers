# Privacy and Release Boundary

This public repository is a curated subset of the private research workspace.
The source of truth for the release decision is
[`public/PUBLIC_RELEASE_MANIFEST.md`](public/PUBLIC_RELEASE_MANIFEST.md).

## Published

- Fictional, constructed benchmark fixtures (`case_x`, `case_m`,
  `case_low_risk`) with digests.
- Aggregate sensitivity, threshold, and combination-rule results.
- Analysis scripts that contain no personal data or local identifiers.
- Study protocol, case briefs, blank rating forms, and recruitment templates
  (with live study URLs redacted).
- Aggregate agreement statistics for both rounds, reported by pseudonymous
  participant ID: `validation/expert-study-cn/round1/round1_agreement.json`
  and `validation/expert-study-cn/round2/round2_results.json`.

## Deliberately excluded (held in the private repository)

- Manuscript sources and preprints, until journal policy is confirmed.
- Reviewer comments, decision letters, response letters, and reviewer
  identities.
- Participant-level data: rating workbooks, identity mappings, eligibility
  corrections, candidate trackers, consent records, and payment records.
- The private AVDM database snapshot and its digest, and the scripts that
  export or identify it.
- Internal planning documents, test data, and backups.

If any file in this repository is found to contain personal, confidential, or
unreleased review information, remove it and rotate the release immediately.
