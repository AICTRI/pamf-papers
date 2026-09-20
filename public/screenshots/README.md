# AVDM Admin UI Screenshots

Screenshots of the AXISRobo-PAMP admin surfaces that configure AVDM, so the
mechanism can be reviewed without installing the platform. They complement
`../reference_config/` (the data) and `../` (the benchmark outputs).

Captured from the software revision tagged `R4.0`, running against the
reference configuration in the `axisarch` database. No participant or client
data is present.

| File | Surface | What it shows |
|---|---|---|
| `01_questionnaire_questions.png` | `/questionnaire-config` → Questions | The 67 managed questionnaire items ordered by stable id, each tagged with its source scope (question bank / questionnaire section / assessment matrix) |
| `02_assessment_matrices.png` | `/questionnaire-config` → Assessment Matrices | The read-only RCP / SCP / PRS complexity matrices, which are rebuilt from the question bank on load |
| `03_concern_mapping_config.png` | `/concern-mapping-config` | The question-answer → concern mapping policy, including the concern × answer score matrix editor |
| `04_classification_policy.png` | `/classification-policy` | The classification thresholds (`0.90` Mandatory / `0.50` Recommended), the complexity coefficient, and the tie-break strategy |

## Reproduce

The screens are not reproducible from the released inputs alone, because they
render the private reference database. They are frozen illustrations of the
navigation and policy model; the authoritative policy values are in
`../reference_config/`.
