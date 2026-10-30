"""Run the evaluation prompts through the Perplexity Agent API. An executor answers
each prompt with the rules file as its system prompt. Two judges score each answer
with the rubric: a stronger model of the same provider, and a model of another one.
Each provider writes its results to RUN_DIR/results/PROVIDER.jsonl, one line for
each score, call, or failure, as soon as it has them. So several processes can run
the providers of one run in parallel, and --merge makes the final view of the run.
Usage: bin/run-evaluation.py [--provider NAME] [--run-id ID] [--all-pairs]
                             [--prompts C1,K1] [--samples N] [--workers N]
                             [--out DIR] [--plan]
       bin/run-evaluation.py --merge RUN_DIR
       bin/run-evaluation.py --agreement RUN_DIR
  --provider   one provider of pairs.json; every provider when left out
  --run-id     the name of the run folder; the UTC time when left out
  --all-pairs  run every pair of each provider, not only the main pair
  --prompts    the prompt IDs to send; every prompt when left out
  --samples    the runs of each prompt (default 3)
  --workers    the units of work in flight at one time (default 4)
  --out        the folder that gets one subfolder per run (default tests/evaluation/results)
  --plan       check pairs.json, print the calls and the cost estimate, call nothing
  --merge      read the JSONL files of a run, and write scores.csv, calls.csv,
               human-test.csv, and summary.md
  --agreement  compare the filled human-test.csv of a run with the judge scores
It reads the key from PERPLEXITY_TOKEN and never prints it. Judges score; they do
not test. The human test of each run is in docs/how-to/run-an-evaluation.md.
"""

import argparse
import csv
import json
import os
import random
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULES = ROOT / "sources" / "model-operating-rules.md"
TESTS = ROOT / "tests" / "evaluation" / "evaluation-tests.md"
PAIRS = ROOT / "tests" / "evaluation" / "pairs.json"
ATTACHMENTS = ROOT / "tests" / "evaluation" / "attachments"
CHECKER = ROOT / "bin" / "deterministic-tests.py"

CRITERIA = [f"R{n}" for n in range(1, 10)]
GATES = {"R1", "R2", "R3", "R5", "R6"}
PASS_SHARE = 0.8
GAP_LIMIT = 3
HUMAN_SAMPLE = 2
# The API refuses a burst of calls with 429, and can drop a long call. Retry
# each call up to ATTEMPTS times, and wait 5, 10, 20, 40 and 80 seconds, or
# the time that the Retry-After header asks for.
ATTEMPTS = 6
RETRY_CODES = (429, 500, 502, 503, 504)
# Tokens of one call, for the --plan estimate only. Each call logs its real cost.
ESTIMATE = {"executor": (6000, 3000), "judge": (12000, 6000)}
CALL_FIELDS = [
    "provider",
    "role",
    "status",
    "model",
    "effort",
    "prompt_id",
    "sample",
    "input_tokens",
    "cache_write_tokens",
    "cache_read_tokens",
    "output_tokens",
    "reasoning_tokens",
    "cost_usd",
    "seconds",
]
HEADER = (
    "date,model,provider,rules_version,prompt_id,domain,grader,"
    + ",".join(CRITERIA)
    + ",total,available,gates_passed,pass,main_defect,response_file"
).split(",")

JUDGE_INSTRUCTIONS = """You score one response of a model with the rubric below. The model had the rules file below as its system prompt, and it answered the prompt in the input.
Score each criterion R1 to R9 with 0, 1, or 2, as the rubric defines them. Score R6 only when the input says that R6 applies. Otherwise give null.
For each score, put the words of the response that support it in evidence, or say what is missing.
The check report comes from a script. Use it for the banned words, the dashes, and the sentence lengths of R9. Do not count them again.
Do not reward length. Do not guess which model wrote the response.
Return only the JSON that the schema asks for.

# Rubric and expected response shape

{rubric}

# Rules file

{rules}
"""

JUDGE_INPUT = """# Prompt {id}

{prompt}

# Expected signals of this prompt

{expected}

R6 applies: {r6}

# Check report

{report}

# Response

{response}
"""


def judge_schema():
    score = {
        "type": "object",
        "additionalProperties": False,
        "required": ["score", "evidence"],
        "properties": {
            # Anthropic rejects minimum and maximum, and Gemini rejects enum, so
            # check_judgment tests the range of each score.
            "score": {"type": ["integer", "null"]},
            "evidence": {"type": "string"},
        },
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "required": ["scores", "main_defect"],
        "properties": {
            "scores": {
                "type": "object",
                "additionalProperties": False,
                "required": CRITERIA,
                "properties": {c: score for c in CRITERIA},
            },
            "main_defect": {"type": "string"},
        },
    }


def check_judgment(judgment):
    """Raise ValueError unless each criterion has a score of 0, 1, 2, or null."""
    for c in CRITERIA:
        value = judgment.get("scores", {}).get(c, {}).get("score", "missing")
        if value not in (0, 1, 2, None) or isinstance(value, bool):
            raise ValueError(f"score of {c} is {value!r}, not 0, 1, 2, or null")


def parse_prompts(text):
    """Read each prompt of evaluation-tests.md Section 1 into a dict."""
    prompts, section, current = [], "", None
    for line in text.splitlines():
        if line.startswith("## ") and current:
            prompts.append(current)
            current = None
        if line.startswith("### "):
            section = line[4:].split(" ", 1)[1]
            if current:
                prompts.append(current)
                current = None
            continue
        start = re.match(r"\*\*Prompt (\w+)", line)
        if start:
            if current:
                prompts.append(current)
            current = {"id": start.group(1), "domain": section, "lines": []}
        elif current is not None:
            current["lines"].append(line)
    if current:
        prompts.append(current)
    for p in prompts:
        body = [line for line in p.pop("lines") if line.strip()]
        p["prompt"] = body[0].strip().strip('"')
        p["expected"] = "\n".join(body[1:])
        # The rubric: R6 scores the prompts of 1.6 and each prompt with a likely wrong answer.
        p["r6"] = p["domain"].startswith("Prompts that invite") or (
            "Likely wrong answer" in p["expected"]
        )
    return prompts


def attach(prompts, folder=ATTACHMENTS):
    """Add the files of attachments/ID/ to the text of prompt ID. The executor and
    the judges get the same text, so a judge can check the numbers of an answer."""
    for p in prompts:
        for path in sorted((folder / p["id"]).glob("*")):
            p["prompt"] += f"\n\n# Attached file: {path.name}\n\n````\n"
            p["prompt"] += path.read_text().rstrip() + "\n````"
    return prompts


def rubric_text(text):
    """Sections 2 and 3 of evaluation-tests.md: the response shape and the rubric."""
    start = text.index("## 2. Expected response shape")
    return text[start : text.index("## 4. Reporting")].strip()


def provider_of(cfg, model):
    for name, provider in cfg["providers"].items():
        if model in provider["ladder"]:
            return name
    return None


def check_pair(cfg, name, pair):
    """Return the reasons that the pair breaks the rule: the judge reasons more."""
    ladder, efforts = cfg["providers"][name]["ladder"], cfg["efforts"]
    ex, judge, second = pair["executor"], pair["judge"], pair.get("second_judge")
    errors = []
    for role, model in (("executor", ex), ("judge", judge)):
        if model["model"] not in ladder:
            errors.append(f"{role} {model['model']} is not in the ladder of {name}")
        if model["effort"] not in efforts:
            errors.append(f"{role} effort {model['effort']} is not a known effort")
    if errors:
        return errors
    rank_ex, rank_judge = ladder.index(ex["model"]), ladder.index(judge["model"])
    if rank_judge > rank_ex or (
        rank_judge == rank_ex
        and efforts.index(judge["effort"]) <= efforts.index(ex["effort"])
    ):
        errors.append(
            f"judge {judge['model']} ({judge['effort']}) does not reason more than "
            f"executor {ex['model']} ({ex['effort']})"
        )
    if second:
        owner = provider_of(cfg, second["model"])
        if owner is None:
            errors.append(f"second judge {second['model']} is in no ladder")
        elif owner == name:
            errors.append(f"second judge {second['model']} is of the same provider")
        if second["effort"] not in efforts:
            errors.append(f"second judge effort {second['effort']} is not known")
    for model in filter(None, (ex, judge, second)):
        if model["model"] not in cfg["prices_usd_per_million"]:
            errors.append(f"{model['model']} has no price")
    return errors


def select_pairs(cfg, provider, all_pairs):
    names = [provider] if provider else list(cfg["providers"])
    for name in names:
        if name not in cfg["providers"]:
            sys.exit(f"pairs.json has no provider {name}")
    return [
        (name, pair)
        for name in names
        for pair in cfg["providers"][name]["pairs"]
        if all_pairs or pair.get("main")
    ]


def judges(pair):
    return [pair["judge"]] + (
        [pair["second_judge"]] if pair.get("second_judge") else []
    )


def plan_cost(cfg, pair, units):
    def cost(model, role):
        tokens_in, tokens_out = ESTIMATE[role]
        price_in, price_out = cfg["prices_usd_per_million"][model["model"]]
        return (tokens_in * price_in + tokens_out * price_out) / 1_000_000

    per_unit = cost(pair["executor"], "executor") + sum(
        cost(j, "judge") for j in judges(pair)
    )
    return per_unit * units


def slug(model):
    return f"{model['model'].replace('/', '_')}@{model['effort']}"


class CallError(RuntimeError):
    """A failed call, with the usage of the API when it billed the call."""

    def __init__(self, message, usage=None):
        super().__init__(message)
        self.usage = usage or {}


def call(cfg, key, model, role, instructions, text, schema=None):
    """One request to the Agent API. Return the text, the usage, and the seconds."""
    body = {
        "model": model["model"],
        "instructions": instructions,
        "input": text,
        "reasoning": {"effort": model["effort"]},
        "max_output_tokens": cfg["max_output_tokens"][role],
    }
    if schema:
        body["response_format"] = {
            "type": "json_schema",
            "json_schema": {"name": "scores", "schema": schema, "strict": True},
        }
    request = urllib.request.Request(
        cfg["endpoint"],
        data=json.dumps(body).encode(),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
    )
    started = time.monotonic()
    for attempt in range(ATTEMPTS):
        wait = 5 * 2**attempt + random.uniform(0, 5)
        try:
            with urllib.request.urlopen(request, timeout=600) as response:
                data = json.load(response)
            break
        except urllib.error.HTTPError as error:
            if error.code not in RETRY_CODES or attempt == ATTEMPTS - 1:
                detail = error.read().decode(errors="replace")[:500]
                raise CallError(f"HTTP {error.code}: {detail}") from None
            asked = error.headers.get("Retry-After", "")
            wait = max(wait, float(asked)) if asked.isdigit() else wait
        # OSError covers URLError, a dropped connection, and a timeout.
        except OSError as error:
            if attempt == ATTEMPTS - 1:
                reason = getattr(error, "reason", None) or error
                raise CallError(f"no connection: {reason}") from None
        time.sleep(wait)
    # Reasoning tokens count toward max_output_tokens, so a model that thinks
    # long can stop in the middle of its answer. Score no cut answer.
    if data.get("status") == "incomplete":
        reason = (data.get("incomplete_details") or {}).get("reason", "unknown")
        used = data.get("usage", {}).get("output_tokens", "?")
        raise CallError(
            f"incomplete answer ({reason}) after {used} output tokens",
            data.get("usage"),
        )
    text = "".join(
        part.get("text", "")
        for item in data.get("output", [])
        if item.get("type") == "message"
        for part in item.get("content", [])
        if part.get("type") == "output_text"
    )
    return text, data.get("usage", {}), time.monotonic() - started


def check_report(path):
    result = subprocess.run(
        [sys.executable, str(CHECKER), "--check", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout


def score(judgment, prompt):
    """Total, available points, gates, and pass of one judgment, per the rubric."""
    scores = {c: judgment["scores"][c]["score"] for c in CRITERIA}
    if not prompt["r6"]:
        scores["R6"] = None
    available = 18 if prompt["r6"] else 16
    total = sum(s for s in scores.values() if s is not None)
    gates = all(
        scores[c] is not None and scores[c] >= 1
        for c in GATES
        if c != "R6" or prompt["r6"]
    )
    return scores, total, available, gates, gates and total >= PASS_SHARE * available


def run_unit(cfg, key, run_dir, ctx, name, pair, prompt, sample):
    """Execute one prompt once, check it, and have each judge score it."""
    ex = pair["executor"]
    stem = f"{prompt['id']}-s{sample}"
    response_file = run_dir / "responses" / slug(ex) / f"{stem}.md"
    response_file.parent.mkdir(parents=True, exist_ok=True)
    calls, rows, errors = [], [], []

    def log(role, model, usage, seconds, status="ok"):
        calls.append(
            {
                "provider": name,
                "role": role,
                "status": status,
                "model": model["model"],
                "effort": model["effort"],
                "prompt_id": prompt["id"],
                "sample": sample,
                # input_tokens includes the tokens written to and read from the cache.
                "input_tokens": usage.get("input_tokens", ""),
                "cache_write_tokens": usage.get("input_tokens_details", {}).get(
                    "cache_creation_input_tokens", ""
                ),
                "cache_read_tokens": usage.get("input_tokens_details", {}).get(
                    "cache_read_input_tokens", ""
                ),
                "output_tokens": usage.get("output_tokens", ""),
                "reasoning_tokens": usage.get("output_tokens_details", {}).get(
                    "reasoning_tokens", ""
                ),
                "cost_usd": usage.get("cost", {}).get("total_cost", ""),
                "seconds": round(seconds, 1),
            }
        )

    try:
        answer, usage, seconds = call(
            cfg, key, ex, "executor", ctx["rules"], prompt["prompt"]
        )
    except CallError as error:
        log("executor", ex, error.usage, 0, "failed")
        return calls, rows, [f"{stem} executor {ex['model']}: {error}"]
    log("executor", ex, usage, seconds)
    response_file.write_text(
        f"{ex['model']}, {name}, {ctx['date']}, {prompt['id']}\n\n{answer}\n"
    )
    report = check_report(response_file)
    for judge in judges(pair):
        text = JUDGE_INPUT.format(
            id=prompt["id"],
            prompt=prompt["prompt"],
            expected=prompt["expected"],
            r6="yes" if prompt["r6"] else "no",
            report=report,
            response=answer,
        )
        try:
            raw, usage, seconds = call(
                cfg, key, judge, "judge", ctx["judge_instructions"], text, ctx["schema"]
            )
        except CallError as error:
            log("judge", judge, error.usage, 0, "failed")
            errors.append(f"{stem} judge {judge['model']}: {error}")
            continue
        try:
            judgment = json.loads(raw)
            check_judgment(judgment)
        except ValueError as error:
            log("judge", judge, usage, seconds, "failed")
            errors.append(f"{stem} judge {judge['model']}: {error}")
            continue
        log("judge", judge, usage, seconds)
        out = run_dir / "judgments" / slug(ex) / f"{stem}.{slug(judge)}.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(judgment, indent=2) + "\n")
        scores, total, available, gates, passed = score(judgment, prompt)
        rows.append(
            {
                "date": ctx["date"],
                "model": f"{ex['model']}@{ex['effort']}",
                "provider": name,
                "rules_version": ctx["version"],
                "prompt_id": prompt["id"],
                "domain": prompt["domain"],
                "grader": f"{judge['model']}@{judge['effort']}",
                **{c: "" if scores[c] is None else scores[c] for c in CRITERIA},
                "total": total,
                "available": available,
                "gates_passed": "yes" if gates else "no",
                "pass": "yes" if passed else "no",
                "main_defect": judgment.get("main_defect", ""),
                "response_file": str(response_file.relative_to(run_dir)),
            }
        )
    return calls, rows, errors


def human_test_rows(rows, seed):
    """The responses a human must score: judges far apart, a failed gate, and a sample."""
    by_file = {}
    for row in rows:
        by_file.setdefault(row["response_file"], []).append(row)
    chosen = {}
    for name, group in by_file.items():
        totals = [r["total"] for r in group]
        if len(totals) > 1 and max(totals) - min(totals) > GAP_LIMIT:
            chosen[name] = "judges differ by more than 3 points"
        elif any(r["gates_passed"] == "no" for r in group):
            chosen[name] = "a judge failed a gate"
    rest = sorted(set(by_file) - set(chosen))
    for name in random.Random(seed).sample(rest, min(HUMAN_SAMPLE, len(rest))):
        chosen[name] = "random sample"
    out = []
    for name, reason in sorted(chosen.items()):
        first = by_file[name][0]
        out.append(
            {
                **{k: first[k] for k in ("date", "model", "provider", "rules_version")},
                **{k: first[k] for k in ("prompt_id", "domain", "response_file")},
                "grader": "human",
                "reason": reason,
            }
        )
    return out


def write_csv(path, rows, fields):
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def token_table(calls):
    """The tokens and cost of each model in each role, from the calls of a run."""
    fields = ["input_tokens", "cache_write_tokens", "cache_read_tokens"]
    fields += ["output_tokens", "reasoning_tokens", "cost_usd"]
    lines = ["## Tokens and cost", ""]
    lines += [
        (
            "| Role | Model | Calls | Input | Cache write | Cache read "
            "| Output | Reasoning | Cost USD |"
        )
    ]
    lines += ["| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    groups = {}
    for c in calls:
        groups.setdefault((c["role"], f"{c['model']}@{c['effort']}"), []).append(c)
    for (role, model), group in sorted(groups.items()):
        sums = {f: sum(float(c.get(f) or 0) for c in group) for f in fields}
        counts = " | ".join(f"{int(sums[f])}" for f in fields[:-1])
        lines.append(
            f"| {role} | {model} | {len(group)} | {counts} | {sums['cost_usd']:.2f} |"
        )
    return lines + [""]


def summary(run_dir, rows, calls, human, errors):
    lines = [f"# Evaluation run {run_dir.name}", ""]
    lines += ["| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |"]
    lines += ["| -------- | ----- | --------- | ---- | ---------- | ---------------- |"]
    groups = {}
    for row in rows:
        groups.setdefault((row["model"], row["grader"]), []).append(row)
    for (model, grader), group in groups.items():
        means = {
            c: sum(int(r[c]) for r in group if r[c] != "")
            / max(1, sum(1 for r in group if r[c] != ""))
            for c in CRITERIA
        }
        lowest = min(means, key=means.get)
        mean = sum(r["total"] for r in group) / len(group)
        passed = sum(r["pass"] == "yes" for r in group)
        lines.append(
            f"| {model} | {grader} | {len(group)} "
            f"| {passed} | {mean:.1f} | {lowest} ({means[lowest]:.2f}) |"
        )
    cost = sum(float(c["cost_usd"]) for c in calls if c["cost_usd"] != "")
    failed = sum(c["status"] == "failed" for c in calls)
    lines += ["", f"Calls: {len(calls)}, {failed} failed. Cost: {cost:.2f} USD.", ""]
    lines += token_table(calls)
    lines += ["## Human test", ""]
    lines += [
        (
            "Score these responses in human-test.csv, then run "
            "`bin/run-evaluation.py --agreement` on this folder."
        ),
        "",
    ]
    lines += [f"- {h['response_file']}: {h['reason']}" for h in human] or ["- none"]
    if errors:
        lines += ["", "## Failed calls", ""]
        lines += [f"- {e['provider']}: {e['message']}" for e in errors]
    (run_dir / "summary.md").write_text("\n".join(lines) + "\n")
    return "\n".join(lines)


def write_records(out, name, calls, rows, errors):
    """Add the results of one unit of work to the JSONL file of its provider."""
    for record in (
        [{"kind": "call", **c} for c in calls]
        + [{"kind": "score", **r} for r in rows]
        + [{"kind": "error", "provider": name, "message": e} for e in errors]
    ):
        out.write(json.dumps(record) + "\n")
    out.flush()


def read_results(run_dir):
    """The scores, calls, and failures of each JSONL file of a run."""
    files = sorted((run_dir / "results").glob("*.jsonl"))
    if not files:
        sys.exit(f"{run_dir / 'results'} has no JSONL file")
    found = {"score": [], "call": [], "error": []}
    for path in files:
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
                found[record.pop("kind")].append(record)
            except (ValueError, KeyError):
                # A process that stops in the middle of a write leaves a cut line.
                found["error"].append(
                    {"provider": path.stem, "message": f"line {number} is not a record"}
                )
    return found["score"], found["call"], found["error"]


def merge(run_dir):
    """Write the final view of a run from the JSONL file of each provider."""
    rows, calls, errors = read_results(run_dir)
    rows.sort(
        key=lambda r: (r["provider"], r["model"], r["response_file"], r["grader"])
    )
    calls.sort(key=lambda c: (c["provider"], c["prompt_id"], c["sample"], c["role"]))
    write_csv(run_dir / "scores.csv", rows, HEADER)
    write_csv(run_dir / "calls.csv", calls, CALL_FIELDS)
    human = human_test_rows(rows, run_dir.name)
    write_csv(run_dir / "human-test.csv", human, HEADER + ["reason"])
    print(summary(run_dir, rows, calls, human, errors))
    return 1 if errors else 0


def agreement(run_dir):
    """Compare the human scores with each judge, criterion by criterion."""
    judged = list(csv.DictReader((run_dir / "scores.csv").open()))
    human = [
        r
        for r in csv.DictReader((run_dir / "human-test.csv").open())
        if r.get("total", "").strip()
    ]
    if not human:
        sys.exit("human-test.csv has no scored row")
    stats = {}
    for h in human:
        for j in (r for r in judged if r["response_file"] == h["response_file"]):
            s = stats.setdefault(j["grader"], {"n": 0, "gap": 0.0, "same": {}})
            s["n"] += 1
            s["gap"] += abs(float(j["total"]) - float(h["total"]))
            for c in CRITERIA:
                if h[c].strip() and j[c].strip():
                    same, count = s["same"].get(c, (0, 0))
                    s["same"][c] = (same + (h[c] == j[c]), count + 1)
    for grader, s in stats.items():
        share = {c: f"{a}/{b}" for c, (a, b) in sorted(s["same"].items())}
        print(f"{grader}: {s['n']} responses, mean total gap {s['gap'] / s['n']:.1f}")
        print(
            "  same score as the human: "
            + ", ".join(f"{c} {v}" for c, v in share.items())
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--provider")
    parser.add_argument("--all-pairs", action="store_true")
    parser.add_argument("--prompts")
    parser.add_argument("--samples", type=int, default=3)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--out", default=str(ROOT / "tests/evaluation/results"))
    parser.add_argument("--pairs", default=str(PAIRS))
    parser.add_argument("--run-id")
    parser.add_argument("--plan", action="store_true")
    parser.add_argument("--merge")
    parser.add_argument("--agreement")
    args = parser.parse_args()
    if args.agreement:
        agreement(Path(args.agreement))
        return 0
    if args.merge:
        return merge(Path(args.merge))

    cfg = json.loads(Path(args.pairs).read_text())
    selected = select_pairs(cfg, args.provider, args.all_pairs)
    problems = [f"{n}: {e}" for n, p in selected for e in check_pair(cfg, n, p)]
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    tests = TESTS.read_text()
    prompts = attach(parse_prompts(tests))
    if args.prompts:
        wanted = args.prompts.split(",")
        unknown = set(wanted) - {p["id"] for p in prompts}
        if unknown:
            sys.exit(f"no prompt {', '.join(sorted(unknown))} in {TESTS.name}")
        prompts = [p for p in prompts if p["id"] in wanted]
    units = len(prompts) * args.samples

    total = 0.0
    for name, pair in selected:
        cost = plan_cost(cfg, pair, units)
        total += cost
        names = " and ".join(slug(j) for j in judges(pair))
        print(
            f"{name}: {slug(pair['executor'])} judged by {names}: {units} units, about {cost:.2f} USD"
        )
    print(f"Estimate for {len(selected)} pairs: about {total:.2f} USD")
    if args.plan:
        return 0

    key = os.environ.get("PERPLEXITY_TOKEN")
    if not key:
        sys.exit(
            "PERPLEXITY_TOKEN is not set. Run with: doppler run --only-secrets PERPLEXITY_TOKEN -- task eval"
        )
    version = json.loads((ROOT / "version.json").read_text())
    now = datetime.now(timezone.utc)
    run_dir = Path(args.out) / (args.run_id or now.strftime("%Y-%m-%dT%H%M%SZ"))
    (run_dir / "results").mkdir(parents=True, exist_ok=True)
    files = {name: run_dir / "results" / f"{name}.jsonl" for name, _ in selected}
    taken = [str(f) for f in files.values() if f.exists()]
    if taken:
        sys.exit(f"{taken[0]} exists. Give the run a new --run-id.")
    ctx = {
        "date": now.strftime("%Y-%m-%d"),
        "version": "{major}.{minor}.{patch}".format(**version),
        "rules": RULES.read_text(),
        "schema": judge_schema(),
        "judge_instructions": JUDGE_INSTRUCTIONS.format(
            rubric=rubric_text(tests), rules=RULES.read_text()
        ),
    }
    work = [
        (name, pair, prompt, sample)
        for name, pair in selected
        for prompt in prompts
        for sample in range(1, args.samples + 1)
    ]
    handles = {name: path.open("a") for name, path in files.items()}
    judged = failed = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(run_unit, cfg, key, run_dir, ctx, *unit): unit[0]
            for unit in work
        }
        for future in as_completed(futures):
            name = futures[future]
            calls, rows, errors = future.result()
            write_records(handles[name], name, calls, rows, errors)
            judged, failed = judged + len(rows), failed + len(errors)
            print(f"{name}: {judged} judgments, {failed} failures", file=sys.stderr)
    for out in handles.values():
        out.close()
    # A failed call is a result too, so the run exits 0 and --merge reports it.
    # In a parallel run, an exit of 1 would stop the other providers.
    print(f"Wrote {', '.join(str(f) for f in files.values())}")
    print(f"Merge with: bin/run-evaluation.py --merge {run_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
