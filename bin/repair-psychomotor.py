"""Send a second turn to the failed psychomotor units of a run, with the sandbox tools.
Usage: bin/repair-psychomotor.py RUN_DIR --mode named|retry --run-id ID [--plan]
It reads RUN_DIR/tool-checks.csv and keeps the failed units whose note is in
NAMED, so each has an answer and a failure that a turn can name. Each unit
starts from the end state of its sandbox, with the prompt, the first answer,
and the second-turn message as its conversation, for up to MAX_STEPS steps.
MODE named states the failure, and MODE retry asks for a check with no
reason, as its control. bin/check-psychomotor.py grades the new run on the
earlier steps and the new steps as one history. It reads the key from
PERPLEXITY_TOKEN and never prints it.
"""

import argparse
import csv
import importlib.util
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(name):
    spec = importlib.util.spec_from_file_location(
        name.replace("-", "_").removesuffix(".py"), ROOT / "bin" / name
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


RUN = load("run-psychomotor.py")
EVAL = RUN.EVAL
MAX_STEPS = 6
# The failures that a second turn can name, and the words that name each.
NAMED = {
    "no check ran after the last write": (
        "No check_file call ran after your last write, so the final state "
        "of the files is unchecked"
    ),
}
NAMED_TEXT = "A reviewer checked your work. {failure}. Fix that with the tools, then answer again."
RETRY_TEXT = "Check your work with the tools, then answer again."
MODES = ("named", "retry")
# One repair unit is a short turn, so its tokens are a third of a full unit.
ESTIMATE = (15000, 2000)


def message(mode, note):
    if mode == "retry":
        return RETRY_TEXT
    return NAMED_TEXT.format(failure=NAMED[note])


def executor_of(slug):
    """The model and effort of a folder name, such as openai_gpt-6.1-sol@medium."""
    name, effort = slug.rsplit("@", 1)
    return {"model": name.replace("_", "/", 1), "effort": effort}


def units(run_dir):
    """Each failed unit of a run that a second turn can name."""
    with (Path(run_dir) / "tool-checks.csv").open() as f:
        rows = list(csv.DictReader(f))
    return [r for r in rows if r["passed"] != "True" and r["note"] in NAMED]


def seed(run_dir, row, mode, prompts):
    """The seed of one repair unit: its sandbox, its conversation, and its steps."""
    run_dir = Path(run_dir)
    stem = f"{row['prompt_id']}-s{row['sample']}"
    transcript = json.loads(
        (run_dir / "transcripts" / row["model"] / f"{stem}.json").read_text()
    )
    return {
        "sandbox": run_dir / "sandbox" / row["model"] / stem,
        "prior_steps": transcript.get("prior_steps", []) + transcript["steps"],
        "max_steps": MAX_STEPS,
        "input": [
            {"role": "user", "content": prompts[row["prompt_id"]]["prompt"]},
            {"role": "assistant", "content": transcript["answer"]},
            {"role": "user", "content": message(mode, row["note"])},
        ],
    }


def rules_of(first):
    """The rules text of the first run. Its file can sit in a removed worktree,
    so fall back to the rules of this checkout when the version is the same."""
    path = Path(first["rules_file"])
    path = path if path.is_absolute() else ROOT / path
    if path.exists():
        return path.read_text()
    here = (ROOT / "sources" / "model-operating-rules.md").read_text()
    if EVAL.rules_version(here) != first["rules_version"]:
        sys.exit(f"{path} is gone, and this checkout has other rules.")
    return here


def plan_cost(cfg, rows):
    tokens_in, tokens_out = ESTIMATE
    total = 0.0
    for r in rows:
        price_in, price_out = cfg["prices_usd_per_million"][
            executor_of(r["model"])["model"]
        ]
        total += (tokens_in * price_in + tokens_out * price_out) / 1_000_000
    return total


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("run_dir")
    parser.add_argument("--mode", choices=MODES, required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--out", default=str(ROOT / "tests/evaluation/results"))
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    cfg = json.loads(EVAL.PAIRS.read_text())
    rows = units(args.run_dir)
    print(f"{len(rows)} repair units, about {plan_cost(cfg, rows):.2f} USD")
    if args.plan or not rows:
        return 0
    key = os.environ.get("PERPLEXITY_TOKEN")
    if not key:
        sys.exit("PERPLEXITY_TOKEN is not set. Run with doppler run.")
    first = json.loads((Path(args.run_dir) / "run.json").read_text())
    rules = rules_of(first)
    out = Path(args.out) / args.run_id
    if out.exists():
        sys.exit(f"{out} exists. Give the run a new --run-id.")
    out.mkdir(parents=True)
    now = datetime.now(timezone.utc)
    ctx = {"date": now.strftime("%Y-%m-%d"), "rules": rules}
    (out / "run.json").write_text(
        json.dumps(
            {
                **first,
                "date": ctx["date"],
                "first_run": str(args.run_dir),
                "mode": args.mode,
                "max_steps": MAX_STEPS,
            },
            indent=2,
        )
        + "\n"
    )
    prompts = {p["id"]: p for p in EVAL.parse_prompts(RUN.PROMPTS_FILE.read_text())}
    errors = []
    with (
        (out / "calls.csv").open("w", newline="") as calls_file,
        ThreadPoolExecutor(max_workers=args.workers) as pool,
    ):
        writer = csv.DictWriter(calls_file, fieldnames=EVAL.CALL_FIELDS)
        writer.writeheader()
        futures = [
            pool.submit(
                RUN.run_unit,
                cfg,
                key,
                out,
                ctx,
                "repair",
                executor_of(r["model"]),
                prompts[r["prompt_id"]],
                int(r["sample"]),
                seed(args.run_dir, r, args.mode, prompts),
            )
            for r in rows
        ]
        for future in as_completed(futures):
            calls, error = future.result()
            writer.writerows(calls)
            calls_file.flush()
            if error:
                errors.append(error)
                with (out / "run.log").open("a") as log:
                    log.write(error + "\n")
    print(
        f"Wrote {out}, {len(errors)} failures. Grade with: bin/check-psychomotor.py {out}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
