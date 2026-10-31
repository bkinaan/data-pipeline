# import json

# from data_pipeline.schema import Invoice

# print(json.dumps(Invoice.model_json_schema(), indent=2))

# inv = Invoice.model_validate(
#     {"order_id": 10248, "order_date": "1996-07-04", "line_items": []}
# )
# print(inv.model_dump(mode="json"))

# try:
#     Invoice.model_validate({"order_date": "July", "bogus_field": 1})
# except Exception as e:
#     print("Rejected as expected:", type(e).__name__)

from pathlib import Path

for p in sorted(Path("../../data/interim/text/").glob("*.txt"))[:3]:
    print("=" * 60, p.name)
    print(p.read_text())