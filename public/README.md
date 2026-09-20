# AVDM Public Validation Fixtures

`case_x_fixture.json`, `case_m_fixture.json`, and `case_low_risk_fixture.json`
are fictional benchmark scenarios. They do not represent an actual company,
client, employee, system, or project.

`case_x_fixture.json` contains only the constructed scenario's normalized
complexity, concern definitions, raw activation totals, reference scores, and
reference classifications. It excludes database names, project identifiers,
usernames, timestamps, contact information, and free text.

Case X was authored for this research and entered into a local AVDM instance
solely to execute and inspect the mechanism. The public fixture is a
metadata-stripped export of that constructed record, not a sanitized observation
of a real project. Cases M and L are deterministic synthetic contrasts generated
from the same frozen 61-item catalog.

Verify each fixture before analysis:

```powershell
Get-ChildItem case_*_fixture.json | Get-FileHash -Algorithm SHA256
```

Expected digests are stored beside the corresponding fixtures.

The reference classifications must remain hidden from recruited architects
until all independent ratings are frozen. Public release should therefore
occur only after data collection closes.

## Input representation

AVDM is questionnaire-driven: only concerns activated by an answer or rule
receive a score, and every other concern receives score zero and classifies as
`Optional`. `Mandatory`/`Recommended` can therefore appear only
among activated concerns, and expert-versus-AVDM agreement is descriptive, not
a controlled comparison. See [`INPUT_REPRESENTATION.md`](INPUT_REPRESENTATION.md).

## Item identifiers

Nine item ids were normalized from legacy slug ids to the canonical code keys
after data collection, and the layer/viewpoint labels were aligned to the
canonical catalog (ratings are unchanged): `app_domain_boundary`→`A5`, `app_resilience_pattern`→`A6`,
`governance_control_matrix`→`AGD6`, `governance_decision_log`→`AGD7`,
`infra_recovery`→`DIN5`, `infra_scalability`→`DIN6`,
`integration_contract`→`IP7`, `integration_dependency_map`→`IP8`,
`security_identity_access`→`SCR11`. The same normalization is applied across the
case briefs, rating forms, reference labels, and questionnaire imports.
