# Blind Expert Comparison Protocol

1. Recruit at least three practicing software or enterprise architects. The
   scenario is fictional and the study is conducted as independent personal
   research without employer sponsorship.
2. Record each participant's role category, architecture experience range, and
   relevant data/integration/security experience. Do not record names in the
   analysis file; assign IDs such as `E1`, `E2`, and `E3`.
3. Give each participant only the screening/consent information and their
   participant-specific workbook. Keep `avdm_reference_private.csv` hidden.
4. Require independent ratings without discussion. Use only `Mandatory`,
   `Recommended`, or `Optional`; do not leave blank ratings.
5. Save completed workbooks as `ratings/E1.xlsx`, `ratings/E2.xlsx`, and so on.
6. Run `analyze_expert_ratings.py` only after all files are frozen.
7. Report participant characteristics, procedure, Fleiss' kappa with its
   interpretation, pairwise exact agreement, agreement with AVDM, and all
   disagreements. Do not claim outcome superiority from agreement alone.

This is an exploratory comparison on one constructed benchmark case. It
tests alignment and reproducibility, not whether either AVDM or experts improve
downstream project outcomes.
