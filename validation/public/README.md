# AVDM Case X Public Validation Fixture

Case X is a fictional benchmark scenario. It does not represent an actual
company, client, employee, system, or project.

`case_x_fixture.json` contains only the constructed scenario's normalized
complexity, concern definitions, raw activation totals, reference scores, and
reference classifications. It excludes database names, project identifiers,
usernames, timestamps, contact information, and free text.

Verify the fixture before analysis:

```powershell
Get-FileHash case_x_fixture.json -Algorithm SHA256
```

The expected digest is stored in `case_x_fixture.sha256`.

The reference classifications must remain hidden from recruited architects
until all independent ratings are frozen. Public release should therefore
occur only after data collection closes.
