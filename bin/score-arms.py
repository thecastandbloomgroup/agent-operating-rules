"""Score two run folders against the marks of a plan.json, with no judge and no API call.
Usage: bin/score-arms.py PLAN_JSON [--control DIR] [--candidate DIR] [--out FILE]
The run folders default to control.run and candidate.run of the plan. Each needs
script-checks.csv (bin/script-checks.py) and calls.csv (bin/run-evaluation.py).
It writes result.json (or FILE) and prints one line per mark. The format of the plan
and the result is in docs/reference/plan-and-result.md. It exits 1 when a mark fails.
"""

import csv
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
Z = 1.96
# Columns of script-checks.csv that hold a count: the check passes when the count is 0.
COUNTS = ("banned", "dashes", "first_person", "long")


def wilson(passes, n):
    """The 95% Wilson interval of passes of n, as (low, high)."""
    if not n:
        return 0.0, 0.0
    p = passes / n
    centre = (p + Z * Z / (2 * n)) / (1 + Z * Z / n)
    half = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / (1 + Z * Z / n)
    return centre - half, centre + half


def newcombe(a, b):
    """The 95% interval of the difference of two rates, b minus a (Newcombe, method 10)."""
    (pa, na), (pb, nb) = a, b
    la, ua = wilson(round(pa * na), na)
    lb, ub = wilson(round(pb * nb), nb)
    d = pb - pa
    low = d - math.sqrt((pb - lb) ** 2 + (ua - pa) ** 2)
    high = d + math.sqrt((ub - pb) ** 2 + (pa - la) ** 2)
    return low, high


def load_arm(run_dir):
    run_dir = Path(run_dir)
    with (run_dir / "script-checks.csv").open() as f:
        rows = list(csv.DictReader(f))
    with (run_dir / "calls.csv").open() as f:
        calls = list(csv.DictReader(f))
    return {"dir": str(run_dir), "rows": rows, "calls": calls}


def passed(row, column):
    if column in COUNTS:
        return row[column] in ("0", "")
    return row[column] == "True"


def share(rows, test):
    n = len(rows)
    return (sum(1 for r in rows if test(r)) / n if n else 0.0), n


def mean_input(calls):
    used = [int(c["input_tokens"] or 0) for c in calls if c.get("status", "ok") == "ok"]
    return sum(used) / len(used) if used else 0.0


def cost(calls):
    return sum(float(c["cost_usd"] or 0) for c in calls)


def rate_record(name, a, b):
    """A record of one rate in both arms, with Wilson intervals and the difference."""
    low, high = newcombe(a, b)
    out = {"metric": name}
    for arm, (p, n) in (("control", a), ("candidate", b)):
        wl, wh = wilson(round(p * n), n)
        out[arm] = {
            "rate": round(p, 4),
            "n": n,
            "wilson_low": round(wl, 4),
            "wilson_high": round(wh, 4),
        }
    out["difference_points"] = round(100 * (b[0] - a[0]), 1)
    out["difference_interval_points"] = [round(100 * low, 1), round(100 * high, 1)]
    return out


def score_mark(mark, control, candidate):
    kind, compare = mark["id"], mark["compare"]
    if kind == "false-lines":
        test = lambda r: bool(r["selftest_wrong"])
        rec = rate_record(
            "share of answers with a false self-test line",
            share(control["rows"], test),
            share(candidate["rows"], test),
        )
        ok = -rec["difference_points"] >= mark["threshold_points"]
        return {**mark, "measures": [rec], "pass": ok}
    if kind == "tokens":
        a, b = mean_input(control["calls"]), mean_input(candidate["calls"])
        fall = 100 * (a - b) / a if a else 0.0
        ok = fall >= mark["threshold_percent"]
        return {
            **mark,
            "measures": [
                {
                    "metric": "mean input tokens per call",
                    "control": round(a, 1),
                    "candidate": round(b, 1),
                    "fall_percent": round(fall, 1),
                }
            ],
            "pass": ok,
        }
    if kind == "cost":
        arms = mark.get("arms", "both")
        spent = cost(candidate["calls"]) + (
            cost(control["calls"]) if arms == "both" else 0.0
        )
        ok = spent < mark["threshold_usd"]
        return {
            **mark,
            "measures": [{"metric": f"cost_usd of {arms}", "value": round(spent, 2)}],
            "pass": ok,
        }
    if compare == "within":
        recs = []
        for column in mark["metric"]:
            test = lambda r, c=column: passed(r, c)
            recs.append(
                rate_record(
                    column, share(control["rows"], test), share(candidate["rows"], test)
                )
            )
        ok = all(abs(r["difference_points"]) <= mark["threshold_points"] for r in recs)
        return {**mark, "measures": recs, "pass": ok}
    raise ValueError(f"mark {kind!r}: unknown id or compare {compare!r}")


def main(argv):
    if not argv:
        sys.exit(__doc__)
    args = list(argv)
    opts = {}
    for flag in ("--control", "--candidate", "--out"):
        if flag in args:
            i = args.index(flag)
            opts[flag] = args[i + 1]
            del args[i : i + 2]
    plan_path = Path(args[0])
    plan = json.loads(plan_path.read_text())
    control = load_arm(opts.get("--control") or ROOT / plan["control"]["run"])
    candidate = load_arm(opts.get("--candidate") or ROOT / plan["candidate"]["run"])
    marks = [score_mark(m, control, candidate) for m in plan["marks"]]
    result = {
        "plan": str(plan_path),
        "control": {
            "run": control["dir"],
            "answers": len(control["rows"]),
            "rules_version": control["rows"][0]["rules_version"]
            if control["rows"]
            else None,
        },
        "candidate": {
            "run": candidate["dir"],
            "answers": len(candidate["rows"]),
            "rules_version": candidate["rows"][0]["rules_version"]
            if candidate["rows"]
            else None,
        },
        "interval": "Wilson 95% per arm; Newcombe 95% for a difference",
        "marks": marks,
        "pass": all(m["pass"] for m in marks),
    }
    out = Path(opts.get("--out") or plan_path.parent / "result.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    for m in marks:
        print(f"{m['id']}: {'pass' if m['pass'] else 'FAIL'}")
    print(f"all marks: {'pass' if result['pass'] else 'FAIL'} -> {out}")
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
