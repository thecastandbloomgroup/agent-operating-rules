"""Have a judge check the domain and the reason of sampled actions of a run.
bin/script-checks.py sees that an action has a domain label and a reason. This
script asks a judge whether the domain is right, per the expected answer of
evaluation-tests.md, whether the reason states cause and effect, and whether it
says how sure that link is.
Usage: bin/judge-actions.py RUN_DIR [--sample 40] [--seed 1] [--actions CSV] [--judge MODEL@EFFORT]
                             [--label DOMAIN] [--prompts X1,T2] [--out NAME] [--plan]
It samples labelled actions round robin across the executors, sends each to a
judge of another provider than its executor, and writes RUN_DIR/action-checks.csv.
--actions takes the file and action of each row of a CSV in place of a sample, so a
second turn is judged on the same actions as its first. A missing action fails every check.
--judge sends every action to one judge in place of that rule, and --out names the CSV.
--label and --prompts sample only the actions with that label, or of those prompts.
It reads the key from PERPLEXITY_TOKEN and never prints it.
"""

import argparse
import csv
import importlib.util
import json
import os
import random
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


EVAL = load("run-evaluation.py")
CHECKS = load("script-checks.py")
# The judge of each action is of another provider than its executor.
JUDGES = {
    "anthropic": {"model": "openai/gpt-6-astra", "effort": "high"},
    "other": {"model": "anthropic/claude-opus-5-5", "effort": "high"},
}
INSTRUCTIONS = """You check one action of an answer that followed a rules file.
Decide three things, each yes or no, from the evidence given.
1. domain_right: the Cynefin domain of this action fits the expected answer of the
   test for this prompt. When the expected answer gives several domains, judge the
   domain of this action in its place in the list. A support step (for example paging a
   responder, naming a channel, or building a measure) does not do the main work of the
   prompt, and it MAY carry its own domain when that domain is right for the step.
2. reason_cause_effect: the reason given for the domain states how cause and effect
   relate in this work (for example "the effect shows only after a trial"), not only
   a restatement of the domain name or of the task. A reason that says what effort it
   takes to know the effect (a known practice, analysis or expertise, a trial, or acting
   first) states it. Judge the reason on its own: a wrong domain does not make it fail.
3. reason_certainty: the reason says how sure the link of cause and effect is. It passes
   when it rests on a known rule or on analysis, or when it rests on cases or trials and
   names what could break the pattern (for example a special cause that throws off an
   estimate), or when no link is visible and acting comes first. A reason that does not
   say how it knows the effect fails. Judge it on its own, as item 2.
Give the domain you expected, and one sentence of note. Judge; do not rewrite."""
INPUT = """Prompt {id}:
{prompt}

Expected answer (evaluation-tests.md):
{expected}

The End section of the answer:
{end}

The action to check (action {index} of End). Its label: {domain}.
{action}
"""
SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "domain_right",
        "expected_domain",
        "reason_cause_effect",
        "reason_certainty",
        "note",
    ],
    "properties": {
        "domain_right": {"type": "boolean"},
        "expected_domain": {"type": "string"},
        "reason_cause_effect": {"type": "boolean"},
        "reason_certainty": {"type": "boolean"},
        "note": {"type": "string"},
    },
}
FIELDS = [
    "executor",
    "file",
    "prompt_id",
    "action",
    "label",
    "script_reason",
    "judge",
    "domain_right",
    "expected_domain",
    "reason_cause_effect",
    "reason_certainty",
    "score",
    "note",
    "cost_usd",
]


def labelled_actions(run_dir):
    """Each labelled action of each answer: (executor, file, prompt ID, index, label, reason, text, End)."""
    out = []
    for path in sorted((Path(run_dir) / "responses").glob("*/*.md")):
        text = path.read_text().split("\n", 2)[-1]
        end = CHECKS.section(text, "End")
        for i, action in enumerate(CHECKS.actions(end), 1):
            domain, reason = CHECKS.label(action)
            if domain:
                out.append(
                    {
                        "executor": path.parent.name,
                        "file": str(path.relative_to(run_dir)),
                        "prompt_id": path.stem.split("-s")[0],
                        "action": i,
                        "label": domain,
                        "script_reason": reason,
                        "text": action.strip(),
                        "end": end.strip(),
                    }
                )
    return out


def only(actions, label, prompts):
    """The actions with the label and of the prompts (a comma list); None keeps all."""
    ids = set(prompts.split(",")) if prompts else None
    return [
        a
        for a in actions
        if (not label or a["label"] == label) and (not ids or a["prompt_id"] in ids)
    ]


def sample(actions, size, seed):
    """Round robin across the executors, each shuffled with the seed."""
    rng = random.Random(seed)
    groups = {}
    for a in actions:
        groups.setdefault(a["executor"], []).append(a)
    for g in groups.values():
        rng.shuffle(g)
    picked, names = [], sorted(groups)
    while len(picked) < size and any(groups.values()):
        for n in names:
            if groups[n] and len(picked) < size:
                picked.append(groups[n].pop())
    return picked


def same_actions(actions, csv_path):
    """The actions at the file and index of each row of csv_path, in its order.
    An action that the second answer lacks comes back with no label."""
    by_key = {(a["file"], a["action"]): a for a in actions}
    with Path(csv_path).open() as f:
        rows = list(csv.DictReader(f))
    return [
        by_key.get(
            (r["file"], int(r["action"])),
            {
                "executor": r["executor"],
                "file": r["file"],
                "prompt_id": r["prompt_id"],
                "action": int(r["action"]),
                "label": "",
            },
        )
        for r in rows
    ]


def missing(a):
    """The row of an action that the answer lacks: both checks fail, at no cost."""
    return {
        **{k: a[k] for k in FIELDS if k in a},
        "judge": "none",
        "domain_right": False,
        "expected_domain": "",
        "reason_cause_effect": False,
        "reason_certainty": False,
        "note": "No labelled action at this index.",
        "score": 0,
        "cost_usd": 0,
    }


def judge_of(executor):
    return JUDGES["anthropic" if executor.startswith("anthropic") else "other"]


def score(result):
    return 2 * bool(result["domain_right"]) + bool(result["reason_cause_effect"])


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("run_dir")
    parser.add_argument("--sample", type=int, default=40)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--actions")
    parser.add_argument("--judge")
    parser.add_argument("--label")
    parser.add_argument("--prompts")
    parser.add_argument("--out", default="action-checks.csv")
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    run_dir = Path(args.run_dir)
    prompts = {
        p["id"]: p for p in EVAL.attach(EVAL.parse_prompts(EVAL.TESTS.read_text()))
    }
    found = only(labelled_actions(run_dir), args.label, args.prompts)
    picked = (
        same_actions(found, args.actions)
        if args.actions
        else sample(found, args.sample, args.seed)
    )
    print(
        f"{len(picked)} actions from {len({a['executor'] for a in picked})} executors"
    )
    if args.plan:
        return 0
    key = os.environ.get("PERPLEXITY_TOKEN")
    if not key:
        sys.exit("PERPLEXITY_TOKEN is not set. Run with doppler run.")
    cfg = json.loads(EVAL.PAIRS.read_text())
    rows, total = [], 0.0
    for a in picked:
        if not a["label"]:
            rows.append(missing(a))
            continue
        p, judge = prompts[a["prompt_id"]], judge_of(a["executor"])
        if args.judge:
            model, effort = args.judge.split("@")
            judge = {"model": model, "effort": effort}
        text = INPUT.format(
            id=p["id"],
            prompt=p["prompt"],
            expected=p["expected"],
            end=a["end"],
            index=a["action"],
            domain=a["label"],
            action=a["text"],
        )
        try:
            raw, usage, _ = EVAL.call(
                cfg, key, judge, "judge", INSTRUCTIONS, text, SCHEMA
            )
            result = json.loads(raw)
        except (EVAL.CallError, ValueError) as error:
            print(f"{a['file']} action {a['action']}: {error}", file=sys.stderr)
            continue
        cost = float(usage.get("cost", {}).get("total_cost") or 0)
        total += cost
        rows.append(
            {
                **{k: a[k] for k in FIELDS if k in a},
                "judge": f"{judge['model']}@{judge['effort']}",
                **{k: result[k] for k in SCHEMA["required"]},
                "score": score(result),
                "cost_usd": cost,
            }
        )
    with (run_dir / args.out).open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    full = sum(1 for r in rows if r["score"] == 3)
    print(f"{full} of {len(rows)} actions score 3. Cost: {total:.2f} USD")
    return 0


if __name__ == "__main__":
    sys.exit(main())
