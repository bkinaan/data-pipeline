from datetime import date
from decimal import Decimal
from pathlib import Path
import json
import sys
import random
import traceback
import re

from data_pipeline.schema import Invoice, LineItem

TEXT_DIR = Path("data/interim/text")
GOLD_DIR = Path("data/gold")
SPLIT_FILE = Path("data/split.json")
LINE_PER_ITEM = 4
PAGE_RE = re.compile(r"Page \d+( of \d+)?", re.IGNORECASE)

def clean_lines(text: str) -> list[str]:
    return [ln.strip() for ln in text.splitlines() if ln.strip()]

def money(s: str) -> Decimal:
    return Decimal(s.replace("$", "").replace(",", ""))

def is_noise(ln: str) -> bool:
    return ln == "Invoice" or bool(PAGE_RE.fullmatch(ln))

def parse_headers(lines: list[str]) -> dict:
    return {
        "order_id": int(re.search(r"\d+", lines[1]).group()),
        "order_date": date.fromisoformat(lines[3].split(" ")[2]),
        "customer": lines[6],
    }
    
def parse_line_items(lines: list[str]) -> list[LineItem]:
    start = lines.index("Unit Price") + 1
    end = next(i for i, ln in enumerate(lines) if ln.startswith("Total"))
    #rows = lines[start:end]
    rows = [ln for ln in lines[start:end] if not is_noise(ln)]
    
    items = []
    for i in range(0, len(rows), LINE_PER_ITEM):
        pid, name, qty, price = rows[i:i + LINE_PER_ITEM]
        items.append(
            LineItem(
                product_id=int(pid),
                product_name=name,
                quantity=int(qty),
                unit_price=money(price),
                line_total=int(qty) * money(price),
            )
        )
    return items

def parse_total(lines: list[str]) -> Decimal:
    idx = next(i for i, ln in enumerate(lines) if ln.startswith("TotalPrice"))
    return money(lines[idx + 1])

def parse_invoice(text: str) -> Invoice:
    lines = clean_lines(text)
    return Invoice(
        **parse_headers(lines),
        line_items=parse_line_items(lines),
        total=parse_total(lines),
    )
    
def run_one(split: dict, stem: str | None) -> None:
    stem = stem or random.choice(split["dev"])
    print("Using", stem)
    text = (TEXT_DIR / f"{stem}.txt").read_text(encoding="utf-8")

    # for i, ln in enumerate(clean_lines(text)):
    #     print(i, repr(ln))
        
    print(parse_invoice(text).model_dump_json(indent=2))
    
def run_batch(split: dict, which: str) -> None:
    stems = split["dev"] + split["eval"] if which == "all" else split[which]
    
    GOLD_DIR.mkdir(parents=True, exist_ok=True)
    failures = {}
    
    for stem in stems:
        try:
            text = (TEXT_DIR / f"{stem}.txt").read_text(encoding="utf-8")
            invoice = parse_invoice(text)
            (GOLD_DIR / f"{stem}.json").write_text(
                invoice.model_dump_json(indent=2), encoding="utf-8"
            )
        except Exception as e:
            failures[stem] = repr(e)
            if len(failures) == 1:
                traceback.print_exc()
                
    print(f"{len(stems) - len(failures)} parsed, {len(failures)} failed ({which})")
    for stem, err in list(failures.items())[:10]:
        print(" ", stem, err)


def main(which: str = "dev", stem: str | None = None) -> None:
    split = json.loads(SPLIT_FILE.read_text())
    
    if which == "one":
        run_one(split, stem)
    else:
        run_batch(split, which)
        
    
if __name__ == "__main__":
    main(
        sys.argv[1] if len(sys.argv) > 1 else "dev",
        sys.argv[2] if len(sys.argv) > 2 else None,
    )