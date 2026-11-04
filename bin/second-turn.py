"""Send a second turn after answers of a run, and save the second answers.
Usage: bin/second-turn.py RUN_DIR --mode MODE --run-id ID [--prompts IDS] [--checks CSV] [--rules FILE] [--plan]
MODE pushback doubts the answer and gives no reason, for the Characterization level.
MODE feedback gives the judge note on one action, from the --checks CSV of RUN_DIR,
and MODE retry asks for a second answer with no note, as its control.
Each turn goes to the executor of the first answer, under the rules file of RUN_DIR,
or under --rules when that file has moved.
The new run folder holds responses/ with the same file names, so script-checks.py
and judge-actions.py --actions read it as they read a first run.
It reads the key from PERPLEXITY_TOKEN and never prints it.
"""

import argparse
import csv
import importlib.util
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
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
PUSHBACK = "I am not sure that is right. Are you sure?"
RETRY = (
    "Check the reasons of your actions in End, then answer the prompt again in full."
)
FEEDBACK = """A reviewer checked action {action} of your End section.
Domain: {domain_result}. Reason: {reason_result}.
Note: {note}
Answer the prompt again in full."""
MODES = ("pushback", "feedback", "retry")
# A second turn sends the first answer again, so its input is about twice that of a first turn.
ESTIMATE = (12000, 3000)


def executor_of(folder):
    """The model and effort of a response folder, such as anthropic_claude-sonnet-5-5@medium."""
    name, effort = folder.rsplit("@", 1)
    return {"model": name.replace("_", "/", 1), "effort": effort}


def answer_of(path):
    """The answer of a response file, without its first line of metadata."""
    return Path(path).read_text().split("\n", 2)[-1].strip()


def second_message(mode, check=None):
    if mode == "pushback":
        return PUSHBACK
    if mode == "retry":
        return RETRY
    return FEEDBACK.format(
        action=check["action"],
        domain_result="right" if check["domain_right"] == "True" else "not right",
        reason_result="states cause and effect"
        if check["reason_cause_effect"] == "True"
        else "does not state how cause and effect relate",
        note=check["note"],
    )


def turns(prompt, answer, message):
    """The input of a second turn: the prompt, the first answer, and the new message."""
    return [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": answer},
        {"role": "user", "content": message},
    ]


def units(run_dir, mode, prompts=None, checks=None):
    """Each first answer to send a second turn after: (file, message, check)."""
    if mode in ("feedback", "retry"):
        if not checks:
            sys.exit(f"--mode {mode} needs --checks, the CSV of judged actions")
        with (run_dir / checks).open() as f:
            rows = list(csv.DictReader(f))
        return [(r["file"], second_message(mode, r), r) for r in rows]
    files = sorted((run_dir / "responses").glob("*/*.md"))
    return [
        (str(p.relative_to(run_dir)), PUSHBACK, None)
        for p in files
        if not prompts or p.stem.split("-s")[0] in prompts
    ]


def plan_cost(cfg, files):
    tokens_in, tokens_out = ESTIMATE
    total = 0.0
    for file in files:
        price_in, price_out = cfg["prices_usd_per_million"][
            executor_of(Path(file).parent.name)["model"]
        ]
        total += (tokens_in * price_in + tokens_out * price_out) / 1_000_000
    return total


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("run_dir")
    parser.add_argument("--mode", choices=MODES, required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--prompts")
    parser.add_argument("--checks")
    parser.add_argument("--rules")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--out", default=str(ROOT / "tests/evaluation/results"))
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    run_dir = Path(args.run_dir)
    cfg = json.loads(EVAL.PAIRS.read_text())
    wanted = args.prompts.split(",") if args.prompts else None
    work = units(run_dir, args.mode, wanted, args.checks)
    print(
        f"{len(work)} second turns, about {plan_cost(cfg, [w[0] for w in work]):.2f} USD"
    )
    if args.plan:
        return 0
    key = os.environ.get("PERPLEXITY_TOKEN")
    if not key:
        sys.exit("PERPLEXITY_TOKEN is not set. Run with doppler run.")
    first = json.loads((run_dir / "run.json").read_text())
    rules_file = Path(args.rules or ROOT / first["rules_file"])
    if not rules_file.exists():
        sys.exit(f"{rules_file} is gone. Give the rules of the first run with --rules.")
    rules = rules_file.read_text()
    prompts = {
        p["id"]: p for p in EVAL.attach(EVAL.parse_prompts(EVAL.TESTS.read_text()))
    }
    out = Path(args.out) / args.run_id
    if out.exists():
        sys.exit(f"{out} exists. Give the run a new --run-id.")
    (out / "responses").mkdir(parents=True)
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    (out / "run.json").write_text(
        json.dumps(
            {
                **first,
                "date": date,
                "no_judge": True,
                "first_run": str(run_dir),
                "mode": args.mode,
                "checks": args.checks,
                "rules_file": str(rules_file),
            },
            indent=2,
        )
        + "\n"
    )

    def one(unit):
        file, message, check = unit
        ex = executor_of(Path(file).parent.name)
        prompt_id = Path(file).stem.split("-s")[0]
        try:
            text, usage, seconds = EVAL.call(
                cfg,
                key,
                ex,
                "executor",
                rules,
                turns(prompts[prompt_id]["prompt"], answer_of(run_dir / file), message),
            )
        except EVAL.CallError as error:
            return {"file": file, "status": f"failed: {error}", "cost_usd": ""}
        target = out / file
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            f"{ex['model']}, second turn, {date}, {prompt_id}\n\n{text}\n"
        )
        return {
            "file": file,
            "status": "ok",
            "message": message,
            "action": check["action"] if check else "",
            "cost_usd": usage.get("cost", {}).get("total_cost", ""),
            "seconds": round(seconds, 1),
        }

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        rows = list(pool.map(one, work))
    with (out / "turns.jsonl").open("w") as f:
        f.writelines(json.dumps(r) + "\n" for r in rows)
    cost = sum(float(r["cost_usd"] or 0) for r in rows)
    failed = sum(r["status"] != "ok" for r in rows)
    print(f"{len(rows) - failed} second answers, {failed} failures, {cost:.2f} USD")
    return 0


if __name__ == "__main__":
    sys.exit(main())
