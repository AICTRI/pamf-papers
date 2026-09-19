# Data Management Plan

## Public After Data Freeze

- Recruitment and screening criteria.
- Consent text and study protocol.
- Fictional case brief and blank rating form.
- Public Case X fixture and its SHA-256 digest.
- Sensitivity and agreement-analysis source code.
- Aggregate agreement statistics and de-identified disagreement counts.
- Per-item rating labels only when every affected participant separately consents.

## Private

- LinkedIn names, profile URLs, email addresses, and direct messages.
- Country, PayPal capability, payment currency, and payment account details.
- Consent records and honorarium/payment records.
- Mapping between real identities and participant IDs.
- Free-text rationales until reviewed for accidental employer or client details.
- Any participant-level data without explicit release consent.
- Private database snapshots and local database identifiers.

## Separation and Retention

- Keep recruitment identities in a private tracker separate from rating files.
- Use only E1, E2, E3, and so on in analysis.
- Freeze submitted workbooks before running analysis.
- Record file hashes and the freeze date.
- Set a deletion date for contact data and identity mappings before recruitment.
- Do not publish combinations of role, region, employer, and detailed experience that could re-identify participants.
