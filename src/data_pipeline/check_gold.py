import json
from decimal import Decimal
from pathlib import Path

from data_pipeline.schema import Invoice

GOLD_DIR = Path("data/gold")
SPLIT = json.loads(Path("data/split.json").read_text())

problems = {}
for stem in SPLIT["dev"]:
    inv = Invoice.model_validate_json((GOLD_DIR / f"{stem}.json").read_text())
    issues = []
    if not inv.line_items:
        issues.append("no line items")
    line_sum = sum((li.line_total for li in inv.line_items), Decimal(0))
    if inv.total is not None and abs(line_sum - inv.total) > Decimal("0.01"):
        issues.append(f"line totals {line_sum} != total {inv.total}")
    if issues:
        problems[stem] = issues
        
print(len(problems), "of", len(SPLIT["dev"]), "have issues")
for stem, issues in list(problems.items())[:15]:
    print(stem, issues)