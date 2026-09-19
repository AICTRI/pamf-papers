from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
VALIDATION = ROOT / "validation"
RESULTS = VALIDATION / "results"
EXPERTS = VALIDATION / "expert-study"
EXPERTS_CN = VALIDATION / "expert-study-cn"
FORMS = VALIDATION / "survey-forms"
