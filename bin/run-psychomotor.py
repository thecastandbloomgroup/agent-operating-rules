"""Run the psychomotor prompts through the Agent API with the sandbox tools.
Each unit copies tests/evaluation/sandbox/<prompt id>/ into the run folder, then
loops: the model answers or calls a tool, bin/tool-sandbox.py runs the call in
the copy, and the result goes back, up to MAX_STEPS calls. The transcript, the
final answer, and the end state of the copy stay in the run folder, and
bin/check-psychomotor.py grades them. No judge model runs.
Usage: bin/run-psychomotor.py [--provider NAME] [--run-id ID] [--prompts P1,P2]
                              [--samples N] [--workers N] [--out DIR]
                              [--rules FILE] [--plan]
The executors are the main pair of each provider of pairs.json. The first run
is also the probe of tool support: a provider that refuses the tools field
fails with an API error in run.log. It reads the key from PERPLEXITY_TOKEN and
never prints it.
"""

import argparse
import csv
import importlib.util
import json
import os
import random
import shutil
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_FILE = ROOT / "tests" / "evaluation" / "psychomotor-tests.md"
FIXTURES = ROOT / "tests" / "evaluation" / "sandbox"


def load(name):
    spec = importlib.util.spec_from_file_location(
        name.replace("-", "_").removesuffix(".py"), ROOT / "bin" / name
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


EVAL = load("run-evaluation.py")
SANDBOX = load("tool-sandbox.py")
MAX_STEPS = 12
# Tokens of one unit for --plan only: the rules go in each step, so the input
# grows with the steps. Each unit logs its real cost in calls.csv.
ESTIMATE = (40000, 5000)


def executors(cfg, provider=None):
    """The executor of the main pair of each provider, as (provider, model)."""
    return [
        (name, pair["executor"])
        for name, pair in EVAL.select_pairs(cfg, provider, all_pairs=False)
    ]


def plan_cost(cfg, model, units):
    tokens_in, tokens_out = ESTIMATE
    price_in, price_out = cfg["prices_usd_per_million"][model["model"]]
    return units * (tokens_in * price_in + tokens_out * price_out) / 1_000_000


def step(cfg, key, model, rules, input_items):
    """One call of the loop. Return the API data and its usage.
    An overloaded job is sent again, as in run-evaluation.py call()."""
    body = {
        "model": model["model"],
        "instructions": rules,
        "input": input_items,
        "reasoning": {"effort": model["effort"]},
        "max_output_tokens": cfg["max_output_tokens"]["executor"],
        "tools": SANDBOX.TOOLS,
        "background": True,
    }
    started = time.monotonic()
    for attempt in range(EVAL.ATTEMPTS):
        data = EVAL.run_job(cfg, key, body, started)
        usage = data.get("usage") or {}
        if data.get("status") not in ("failed", "cancelled"):
            break
        detail = (data.get("error") or {}).get("message", "no detail")
        if "overloaded" not in detail.lower() or attempt == EVAL.ATTEMPTS - 1:
            raise EVAL.CallError(f"{data['status']}: {detail}", usage)
        time.sleep(5 * 2**attempt + random.uniform(0, 5))
    if data.get("status") == "incomplete":
        reason = (data.get("incomplete_details") or {}).get("reason", "unknown")
        raise EVAL.CallError(f"incomplete answer ({reason})", usage)
    return data, usage, time.monotonic() - started


def answer_text(output):
    return "".join(
        part.get("text", "")
        for item in output
        if item.get("type") == "message"
        for part in item.get("content", [])
        if part.get("type") == "output_text"
    )


def run_unit(cfg, key, run_dir, ctx, name, model, prompt, sample):
    """One prompt in one fresh sandbox copy. Return (calls, error or None)."""
    slug = EVAL.slug(model)
    stem = f"{prompt['id']}-s{sample}"
    sandbox_dir = run_dir / "sandbox" / slug / stem
    shutil.copytree(FIXTURES / prompt["id"], sandbox_dir)
    transcript = {"model": slug, "prompt_id": prompt["id"], "sample": sample}
    steps, calls, error = [], [], None
    input_items = [{"role": "user", "content": prompt["prompt"]}]
    for _ in range(MAX_STEPS):
        try:
            data, usage, seconds = step(cfg, key, model, ctx["rules"], input_items)
        except EVAL.CallError as exc:
            error, usage = f"{stem} {model['model']}: {exc}", exc.usage
            calls.append(log_row(name, model, prompt, sample, usage, 0, "failed"))
            break
        calls.append(log_row(name, model, prompt, sample, usage, seconds))
        output = data.get("output", [])
        input_items = input_items + output
        tool_calls = [item for item in output if item.get("type") == "function_call"]
        if not tool_calls:
            transcript["answer"] = answer_text(output)
            break
        for call in tool_calls:
            try:
                arguments = json.loads(call.get("arguments") or "{}")
            except json.JSONDecodeError:
                arguments, result, violation = {}, "refused: bad arguments", None
            else:
                result, violation = SANDBOX.execute(
                    sandbox_dir, call.get("name", ""), arguments
                )
            steps.append(
                {
                    "name": call.get("name"),
                    "arguments": arguments,
                    "output": result[:2000],
                    "violation": violation,
                }
            )
            input_items.append(
                {
                    "type": "function_call_output",
                    "call_id": call.get("call_id"),
                    "output": result,
                }
            )
    else:
        error = f"{stem} {model['model']}: no answer after {MAX_STEPS} steps"
    transcript["steps"] = steps
    transcript["violations"] = [s["violation"] for s in steps if s["violation"]]
    if error:
        transcript["error"] = error
    out = run_dir / "transcripts" / slug / f"{stem}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(transcript, indent=2) + "\n")
    if "answer" in transcript:
        response = run_dir / "responses" / slug / f"{stem}.md"
        response.parent.mkdir(parents=True, exist_ok=True)
        response.write_text(
            f"{model['model']}, {name}, {ctx['date']}, {prompt['id']}\n\n"
            f"{transcript['answer']}\n"
        )
    return calls, error


def log_row(name, model, prompt, sample, usage, seconds, status="answered"):
    row = dict.fromkeys(EVAL.CALL_FIELDS, "")
    row.update(
        provider=name,
        role="executor",
        status=status,
        model=model["model"],
        effort=model["effort"],
        prompt_id=prompt["id"],
        sample=sample,
        input_tokens=usage.get("input_tokens", 0),
        output_tokens=usage.get("output_tokens", 0),
        cost_usd=usage.get("cost", {}).get("total_cost", 0),
        seconds=round(seconds, 1),
    )
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--provider")
    parser.add_argument("--run-id")
    parser.add_argument("--prompts")
    parser.add_argument("--samples", type=int, default=3)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--out", default=str(ROOT / "tests/evaluation/results"))
    parser.add_argument("--rules", default=str(EVAL.RULES))
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    cfg = json.loads(EVAL.PAIRS.read_text())
    wanted = args.prompts.split(",") if args.prompts else None
    prompts = [
        p
        for p in EVAL.parse_prompts(PROMPTS_FILE.read_text())
        if not wanted or p["id"] in wanted
    ]
    if not prompts:
        sys.exit(f"no prompt of {args.prompts} is in {PROMPTS_FILE}")
    selected = executors(cfg, args.provider)
    units = len(prompts) * args.samples
    cost = sum(plan_cost(cfg, model, units) for _, model in selected)
    print(
        f"{units * len(selected)} units of up to {MAX_STEPS} steps, "
        f"about {cost:.2f} USD"
    )
    if args.plan:
        return 0
    key = os.environ.get("PERPLEXITY_TOKEN")
    if not key:
        sys.exit("PERPLEXITY_TOKEN is not set. Run with doppler run.")
    now = datetime.now(timezone.utc)
    run_id = args.run_id or now.strftime("%Y-%m-%dT%H%M%SZ-psychomotor")
    run_dir = Path(args.out) / run_id
    if run_dir.exists():
        sys.exit(f"{run_dir} exists. Give the run a new --run-id.")
    run_dir.mkdir(parents=True)
    rules = Path(args.rules).read_text()
    ctx = {"date": now.strftime("%Y-%m-%d"), "rules": rules}
    (run_dir / "run.json").write_text(
        json.dumps(
            {
                "date": ctx["date"],
                "rules_version": EVAL.rules_version(rules),
                "rules_file": args.rules,
                "prompts": [p["id"] for p in prompts],
                "samples": args.samples,
                "max_steps": MAX_STEPS,
            },
            indent=2,
        )
        + "\n"
    )
    work = [
        (name, model, prompt, sample)
        for name, model in selected
        for prompt in prompts
        for sample in range(1, args.samples + 1)
    ]
    all_calls, errors = [], []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [
            pool.submit(run_unit, cfg, key, run_dir, ctx, *unit) for unit in work
        ]
        for future in as_completed(futures):
            calls, error = future.result()
            all_calls.extend(calls)
            if error:
                errors.append(error)
            done = sum(1 for f in futures if f.done())
            print(
                f"{done} of {len(work)} units, {len(errors)} failures", file=sys.stderr
            )
    with (run_dir / "calls.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=EVAL.CALL_FIELDS)
        writer.writeheader()
        writer.writerows(all_calls)
    if errors:
        (run_dir / "run.log").write_text("\n".join(sorted(errors)) + "\n")
    # A failed unit is a result too, so the run exits 0 and the log names it.
    print(f"Wrote {run_dir}. Grade with: bin/check-psychomotor.py {run_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
