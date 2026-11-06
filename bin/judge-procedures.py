"""Have a judge score the procedure of each passed P7 unit of a psychomotor run.
Usage: bin/judge-procedures.py RUN_DIR [--plan]
It reads RUN_DIR/tool-checks.csv (bin/check-psychomotor.py), and for each passed
P7 unit it sends notes/procedure.md of its sandbox to a judge of another
provider than the executor. The judge sees only the procedure. It scores three
criteria 0, 1, or 2, and the weighted score runs from 0 to 100. The rubric is in
tests/evaluation/results/2026-11-06-p7-quality-plan.md. A procedure passes at 85
or more with no criterion at 0, per the addendum of the P1 to P7 results. It writes
RUN_DIR/procedure-checks.csv, and reads the key from PERPLEXITY_TOKEN.
"""

import argparse
import csv
import importlib.util
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(name):
    spec = importlib.util.spec_from_file_location(
        name.replace("-", "_"), ROOT / "bin" / name
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


JUDGE = load("judge-actions.py")
WEIGHTS = {"complete": 40, "executable": 30, "general": 30}
# 70 let a procedure pass with two steps that need a guess (0 on executable).
PASS_MARK = 85
INSTRUCTIONS = """You score one procedure that an agent wrote for other agents.
The task of the procedure: make one notes file pass the checks for banned words and
sentences over 25 words, with the tools list_files, read_file, write_file, and
check_file. The agent then used it on three files, notes/a.md, notes/b.md, notes/c.md.
Score each criterion 0, 1, or 2, from the text of the procedure only.
1. complete: 2 when the steps cover a check, a fix of banned words, a fix of long
   sentences, a write of the file, and a check again until clean. 1 when one of these
   is missing. 0 when two or more are missing.
2. executable: 2 when each step names a tool or an action that another agent can do
   with no guess. 1 when one step needs a guess. 0 when two or more steps need a guess.
3. general: 2 when no step names a.md, b.md, c.md, or their content. 1 when one step
   names them. 0 when the steps work only for these files.
Give one sentence of note. Score; do not rewrite."""
SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["complete", "executable", "general", "note"],
    "properties": {
        "complete": {"type": "integer"},
        "executable": {"type": "integer"},
        "general": {"type": "integer"},
        "note": {"type": "string"},
    },
}


def passes(scores):
    """A procedure passes at PASS_MARK or more, with no criterion at 0."""
    return weighted(scores) >= PASS_MARK and min(int(scores[k]) for k in WEIGHTS) > 0


def weighted(scores):
    """The weighted score from 0 to 100 of scores of 0, 1, or 2 per criterion."""
    return sum(WEIGHTS[k] * max(0, min(2, int(scores[k]))) / 2 for k in WEIGHTS)


def passed_p7(run_dir):
    with (Path(run_dir) / "tool-checks.csv").open() as f:
        return [
            r
            for r in csv.DictReader(f)
            if r["prompt_id"] == "P7" and r["passed"] == "True"
        ]


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("run_dir")
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    run_dir = Path(args.run_dir)
    units = passed_p7(run_dir)
    print(f"{len(units)} passed P7 units")
    if args.plan:
        return 0
    key = os.environ.get("PERPLEXITY_TOKEN")
    if not key:
        sys.exit("PERPLEXITY_TOKEN is not set. Run with doppler run.")
    cfg = json.loads(JUDGE.EVAL.PAIRS.read_text())
    rows, total = [], 0.0
    for u in units:
        folder = u["model"].replace("/", "_")
        procedure = (
            run_dir / "sandbox" / folder / f"P7-s{u['sample']}" / "notes/procedure.md"
        )
        judge = JUDGE.judge_of(folder)
        try:
            raw, usage, _ = JUDGE.EVAL.call(
                cfg, key, judge, "judge", INSTRUCTIONS, procedure.read_text(), SCHEMA
            )
            result = json.loads(raw)
        except (JUDGE.EVAL.CallError, ValueError) as error:
            print(f"{folder} P7-s{u['sample']}: {error}", file=sys.stderr)
            continue
        cost = float(usage.get("cost", {}).get("total_cost") or 0)
        total += cost
        score = weighted(result)
        rows.append(
            {
                "model": u["model"],
                "sample": u["sample"],
                "judge": f"{judge['model']}@{judge['effort']}",
                **{k: result[k] for k in WEIGHTS},
                "score": score,
                "passed": passes(result),
                "note": result["note"],
                "cost_usd": cost,
            }
        )
    if not rows:
        sys.exit("no procedure was judged")
    with (run_dir / "procedure-checks.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    good = sum(r["passed"] for r in rows)
    print(
        f"{good} of {len(rows)} procedures pass: {PASS_MARK} or more, no criterion at 0. Cost: {total:.2f} USD"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
