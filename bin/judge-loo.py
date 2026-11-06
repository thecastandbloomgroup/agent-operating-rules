"""Judge each marked row with the human marks of the other rows as examples.
The sheet of a human marking session holds one mark per row. For each row, this
script gives the judge the other rows with their human marks and notes, then asks
it to judge the row held out. It prints the agreement and kappa with the human.
Usage: bin/judge-loo.py MARKING_DIR [--judge MODEL@EFFORT] [--out CSV] [--no-expected] [--plan]
--no-expected leaves the expected answer of the test out of each call, and asks
whether the label fits the work of the action, as the marking page asks the human.
With no --judge, each row goes to a judge of another provider than its executor.
MARKING_DIR holds sheet.csv and items.json. It reads the key from PERPLEXITY_TOKEN.
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
EXAMPLES = """
A human marker judged other actions of the same kind. On domain_right, the human
answer is the standard. Read the notes for why the human said no, or what the human
saw that the label misses, and judge this action the way the human would.
{examples}"""
EXAMPLE = """
Example {n}. Prompt {prompt_id}: {prompt}
Its label: {label}.
{action}
Human answer: domain_right {domain}, reason_cause_effect {reason}. Note: {note}
"""
WORK = """1. domain_right: the Cynefin domain of this action fits the work of this action,
   that is, how cause and effect relate in what this step does. Judge the step itself
   against these definitions, the same ones the human saw:
   - Clear: cause and effect are known to everyone. A best practice exists. One step.
   - Complicated: cause and effect are knowable with analysis or expertise.
   - Complex: cause and effect are visible only afterward. A small, safe-to-fail probe.
   - Chaotic: no cause and effect are visible. The action stabilises first.
   - Confused: the domain cannot be told. The action gathers what is needed to classify.
2. reason_cause_effect:"""
NO_EXPECTED = "Expected answer (evaluation-tests.md):\n{expected}\n\n"


def instructions_of(no_expected):
    """The built-in instruction, with item 1 judged against the work when no_expected."""
    if not no_expected:
        return JUDGE.INSTRUCTIONS
    start = JUDGE.INSTRUCTIONS.index("1. domain_right:")
    end = JUDGE.INSTRUCTIONS.index("2. reason_cause_effect:")
    return (
        JUDGE.INSTRUCTIONS[:start]
        + WORK
        + JUDGE.INSTRUCTIONS[end + len("2. reason_cause_effect:") :]
    )


def input_of(no_expected):
    """The input template of each call, with no expected answer when no_expected."""
    return JUDGE.INPUT.replace(NO_EXPECTED, "") if no_expected else JUDGE.INPUT


def truth(text):
    return text.strip().lower() == "true"


def examples(items, marks, held):
    """The example block of every row but the held one, numbered from 1."""
    parts = [
        EXAMPLE.format(
            n=n,
            prompt_id=item["prompt_id"],
            prompt=item["prompt"],
            label=item["label"],
            action=item["action_text"].strip(),
            domain=mark["domain_right_human"],
            reason=mark["reason_cause_effect_human"],
            note=mark["note"].strip() or "none",
        )
        for n, (item, mark) in enumerate(
            ((i, m) for k, (i, m) in enumerate(zip(items, marks)) if k != held), 1
        )
    ]
    return EXAMPLES.format(examples="".join(parts))


def kappa(x, y):
    n = len(x)
    observed = sum(a == b for a, b in zip(x, y)) / n
    chance = sum((x.count(c) / n) * (y.count(c) / n) for c in (True, False))
    return observed, (observed - chance) / (1 - chance) if chance < 1 else 0.0


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("marking_dir")
    parser.add_argument("--judge")
    parser.add_argument("--out", default="loo.csv")
    parser.add_argument("--no-expected", action="store_true")
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    folder = Path(args.marking_dir)
    items = json.loads((folder / "items.json").read_text())
    with (folder / "sheet.csv").open() as f:
        marks = list(csv.DictReader(f))
    if len(items) != len(marks):
        sys.exit("items.json and sheet.csv differ in length")
    print(f"{len(items)} rows, one call each")
    if args.plan:
        return 0
    key = os.environ.get("PERPLEXITY_TOKEN")
    if not key:
        sys.exit("PERPLEXITY_TOKEN is not set. Run with doppler run.")
    cfg = json.loads(JUDGE.EVAL.PAIRS.read_text())
    prompts = {
        p["id"]: p
        for p in JUDGE.EVAL.attach(
            JUDGE.EVAL.parse_prompts(JUDGE.EVAL.TESTS.read_text())
        )
    }
    rows, total = [], 0.0
    for k, (item, mark) in enumerate(zip(items, marks)):
        p = prompts[item["prompt_id"]]
        judge = JUDGE.judge_of(item["file"].split("/")[1])
        if args.judge:
            model, effort = args.judge.split("@")
            judge = {"model": model, "effort": effort}
        text = input_of(args.no_expected).format(
            id=p["id"],
            prompt=p["prompt"],
            expected=p["expected"],
            end=item["end"],
            index=item["action"],
            domain=item["label"],
            action=item["action_text"],
        )
        instructions = (
            instructions_of(args.no_expected) + "\n" + examples(items, marks, k)
        )
        try:
            raw, usage, _ = JUDGE.EVAL.call(
                cfg, key, judge, "judge", instructions, text, JUDGE.SCHEMA
            )
            result = json.loads(raw)
        except (JUDGE.EVAL.CallError, ValueError) as error:
            print(f"row {k + 1}: {error}", file=sys.stderr)
            continue
        cost = float(usage.get("cost", {}).get("total_cost") or 0)
        total += cost
        rows.append(
            {
                "row": k + 1,
                "file": item["file"],
                "action": item["action"],
                "label": item["label"],
                "human_domain": mark["domain_right_human"],
                "judge": f"{judge['model']}@{judge['effort']}",
                **{f: result[f] for f in JUDGE.SCHEMA["required"]},
                "cost_usd": cost,
            }
        )
    with (folder / args.out).open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    human = [truth(r["human_domain"]) for r in rows]
    judged = [bool(r["domain_right"]) for r in rows]
    agree, k = kappa(human, judged)
    print(
        f"label: {round(agree * len(rows))} of {len(rows)}, kappa {k:.2f}. Cost: {total:.2f} USD"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
