# Run once to create the dev and eval set lists
import json
import random
from pathlib import Path

TEXT_DIR = Path("data/interim/text")
SPLIT_FILE = Path("data/split.json")
EVAL_SIZE = 100
SEED = 42

stems = sorted(p.stem for p in TEXT_DIR.glob("*.txt"))

rng = random.Random(SEED)
eval_stems = sorted(rng.sample(stems, EVAL_SIZE))
eval_set = set(eval_stems)
dev_stems = [s for s in stems if s not in eval_set]

SPLIT_FILE.parent.mkdir(parents=True, exist_ok=True)
SPLIT_FILE.write_text(
    json.dumps({"seed": SEED, "eval": eval_stems, "dev": dev_stems}, indent=2)
)
print(len(dev_stems), "dev,", len(eval_stems), "eval")