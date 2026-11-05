"""Write the items of a marking sheet: the prompt, the End section, and the action text.
Usage: bin/marking-items.py SHEET_DIR
It reads SHEET_DIR/sheet.csv (columns run, file, action, and the mark columns) and
writes SHEET_DIR/items.json, one item per row, in sheet order. Each item holds the
prompt text, the End section, and the action, found with the parsers of
bin/script-checks.py. It holds no judge result, so a person marks blind.
The app in tools/marking reads items.json and writes the marks back to sheet.csv.
"""

import csv
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "tests" / "evaluation" / "results"


def load(name):
    spec = importlib.util.spec_from_file_location(
        name.replace("-", "_").removesuffix(".py"), ROOT / "bin" / name
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


EVAL = load("run-evaluation.py")
CHECKS = load("script-checks.py")


def item(row, prompts, results=RESULTS):
    """One sheet row as an item for the app."""
    path = results / row["run"] / row["file"]
    text = path.read_text().split("\n", 2)[-1]
    end = CHECKS.section(text, "End")
    actions = CHECKS.actions(end)
    index = int(row["action"])
    action = actions[index - 1].strip() if 0 < index <= len(actions) else ""
    domain, _ = CHECKS.label(action) if action else (None, False)
    prompt_id = Path(row["file"]).stem.split("-s")[0]
    return {
        "run": row["run"],
        "file": row["file"],
        "action": index,
        "prompt_id": prompt_id,
        "prompt": prompts.get(prompt_id, ""),
        "label": domain or "",
        "action_text": action,
        "end": end.strip(),
    }


def main(argv):
    if len(argv) != 2:
        sys.exit(__doc__.split("\n")[1])
    sheet_dir = Path(argv[1])
    with (sheet_dir / "sheet.csv").open() as f:
        rows = list(csv.DictReader(f))
    prompts = {p["id"]: p["prompt"] for p in EVAL.parse_prompts(EVAL.TESTS.read_text())}
    items = [item(r, prompts) for r in rows]
    missing = [i for i in items if not i["action_text"]]
    (sheet_dir / "items.json").write_text(json.dumps(items, indent=2) + "\n")
    print(f"Wrote {len(items)} items, {len(missing)} with no action text")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
