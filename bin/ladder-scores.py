"""Score each model on the Bloom ladders of the evaluation design, from the checks of runs.
Usage: bin/ladder-scores.py [--json] RUN_DIR [RUN_DIR ...]
--json also writes RUN_DIR/ladder-scores.json for each run: one record per model,
ladder and level, in the schema of docs/reference/ladder-scores.schema.json.
It reads RUN_DIR/script-checks.csv (bin/script-checks.py) and, when present,
RUN_DIR/action-checks.csv and RUN_DIR/action-checks-argon.csv (bin/judge-actions.py)
and RUN_DIR/tool-checks.csv (bin/check-psychomotor.py), the psychomotor trials.
Evaluate counts the self-test lines that the script checks, except the word counts.
Each check counts as one trial of one level (MAP). A level passes at 80% of 20
trials or more. The score of a taxonomy is (L + p) / N, where L is the highest level
passed with every measured level below it passed, p is the rate of the next
level, and N counts the measured levels. When a pass rate rises by more than 5
points from one measured level to the next, the levels are not cumulative for
that model, and the score is the mean rate of the measured levels (design note,
Follow-up). A rate from fewer than 20 trials is marked with an asterisk, and a
taxonomy with such a level gets no score, because one answer could flip it. The
combined score is the geometric mean of the three taxonomies, and it is reported
only when all three are measured.
"""

import collections
import csv
import itertools
import json
import math
import sys
from pathlib import Path

LADDERS = {
    "cognitive": ["Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"],
    "affective": [
        "Receiving",
        "Responding",
        "Valuing",
        "Organization",
        "Characterization",
    ],
    "psychomotor": [
        "Perception",
        "Set",
        "Guided response",
        "Mechanism",
        "Complex overt response",
        "Adaptation",
        "Origination",
    ],
}
# The level of the structure check of each prompt of tests 1.7. Other prompts: Receiving.
AFFECTIVE = {"A1": "Responding", "A2": "Valuing", "A3": "Organization"}
PASS_RATE, MIN_TRIALS, TOLERANCE = 0.8, 20, 0.05
SCHEMA_VERSION = "1.0"
# The levels that a judge grades, with the lower kappa of the two judges against a
# person (judge trust results, 2026-11-05). A trial needs both judges, so the lower one
# bounds it. The kit trusts a judged level only at a kappa of 0.667 or more.
KAPPA_SOURCE = "tests/evaluation/results/2026-11-05-judge-trust-results.md"
JUDGED = {"Understand": 0.08, "Analyze": -0.40}
# Self-test lines that count words. The models write 0 whatever the count, and a count is
# the checker's job, so Evaluate leaves them out (2026-11-03 factored self-test probe).
WORD_COUNTS = ("Sentences over", "Longest sentence")


def judged_right(row):
    """True when each self-test line that the script checks, other than a word count, is right."""
    wrong = [k for k in row["selftest_wrong"].split(";") if k]
    return int(row["selftest_lines"]) > 0 and all(
        k.startswith(WORD_COUNTS) for k in wrong
    )


def trials(run_dir):
    """Each (model, taxonomy, level, passed) of the checks of one run."""
    run_dir = Path(run_dir)
    out = []
    path = run_dir / "script-checks.csv"
    if path.exists():
        with path.open() as f:
            for r in csv.DictReader(f):
                m, yes = r["model"], lambda k, r=r: r[k] == "True"
                out.append(
                    (
                        m,
                        "affective",
                        AFFECTIVE.get(r["prompt_id"], "Receiving"),
                        yes("structure"),
                    )
                )
                if r["prompt_id"] not in AFFECTIVE:
                    out.append((m, "cognitive", "Apply", yes("language")))
                    out.append((m, "cognitive", "Apply", yes("all_labelled")))
                    out.append((m, "cognitive", "Evaluate", judged_right(r)))
    path = run_dir / "tool-checks.csv"
    if path.exists():
        with path.open() as f:
            for r in csv.DictReader(f):
                out.append(
                    (r["model"], "psychomotor", r["level"], r["passed"] == "True")
                )
    judged = [run_dir / n for n in ("action-checks.csv", "action-checks-argon.csv")]
    if all(p.exists() for p in judged):
        checks = collections.defaultdict(list)
        for p in judged:
            with p.open() as f:
                for r in csv.DictReader(f):
                    checks[(r["executor"], r["file"], r["action"])].append(r)
        for (m, _, _), rs in checks.items():
            # A trial passes only when both judges say yes.
            out.append(
                (
                    m,
                    "cognitive",
                    "Understand",
                    all(r["reason_cause_effect"] == "True" for r in rs),
                )
            )
            out.append(
                (
                    m,
                    "cognitive",
                    "Analyze",
                    all(r["domain_right"] == "True" for r in rs),
                )
            )
    return out


def ladder(rows, taxonomy):
    """Each level of one taxonomy as (level, passed, n), with n = 0 when not measured."""
    count = collections.Counter((lv, ok) for t, lv, ok in rows if t == taxonomy)
    return [
        (lv, count[(lv, True)], count[(lv, True)] + count[(lv, False)])
        for lv in LADDERS[taxonomy]
    ]


def cumulative(levels):
    """True when no pass rate rises by more than TOLERANCE from one measured level to the next."""
    rates = [ok / n for _, ok, n in levels if n]
    return all(b <= a + TOLERANCE for a, b in itertools.pairwise(rates))


def score(levels):
    """(L, p, N, score, cumulative) over the measured levels, or None when none is measured.
    When the levels are not cumulative, L is None and the score is the mean rate."""
    measured = [(lv, ok, n) for lv, ok, n in levels if n]
    if not measured:
        return None
    short = [lv for lv, _, n in measured if n < MIN_TRIALS]
    if short:
        return None, None, len(measured), None, short
    if not cumulative(measured):
        mean = sum(ok / n for _, ok, n in measured) / len(measured)
        return None, None, len(measured), mean, False
    passed = 0
    for _, ok, n in measured:
        if n >= MIN_TRIALS and ok / n >= PASS_RATE:
            passed += 1
        else:
            break
    nxt = measured[passed][1] / measured[passed][2] if passed < len(measured) else 0.0
    return passed, nxt, len(measured), (passed + nxt) / len(measured), True


def report(run_dirs):
    rows = [t for d in run_dirs for t in trials(d)]
    per_model = collections.defaultdict(list)
    for m, t, lv, ok in rows:
        per_model[m].append((t, lv, ok))
    per_model["All"] = [(t, lv, ok) for m, t, lv, ok in rows]
    out = []
    for taxonomy, names in LADDERS.items():
        models = sorted(m for m in per_model if m != "All") + ["All"]
        out += [f"### {taxonomy.capitalize()}", ""]
        out.append("| Level | " + " | ".join(models) + " |")
        out.append("| --- " * (len(models) + 1) + "|")
        for i, lv in enumerate(names):
            cells = []
            for m in models:
                _, ok, n = ladder(per_model[m], taxonomy)[i]
                star = "*" if n and n < MIN_TRIALS else ""
                cells.append(f"{ok / n:.0%} of {n}{star}" if n else "not measured")
            out.append(f"| {lv} | " + " | ".join(cells) + " |")
        cells = []
        for m in models:
            s = score(ladder(per_model[m], taxonomy))
            if not s:
                cells.append("not measured")
            elif isinstance(s[4], list):
                cells.append("too few trials: " + ", ".join(s[4]))
            elif s[4]:
                cells.append(f"{s[3]:.2f} (L={s[0]})")
            else:
                cells.append(f"{s[3]:.2f} (mean, not cumulative)")
        out.append("| Score (L + p) / N | " + " | ".join(cells) + " |")
        out += [
            "",
            "* fewer than 20 trials, so the level cannot count as passed.",
            "",
        ]
    scores = {t: score(ladder(per_model["All"], t)) for t in LADDERS}
    if all(s and s[3] is not None for s in scores.values()):
        product = 1.0
        for s in scores.values():
            product *= s[3]
        out.append(f"Combined score (All): {product ** (1 / 3):.2f}")
    else:
        missing = ", ".join(t for t, s in scores.items() if not s or s[3] is None)
        out.append(f"Combined score: not reported. No score yet: {missing}.")
    return "\n".join(out)


def wilson(passes, n, z=1.96):
    """The 95% Wilson interval of passes of n, as (low, high)."""
    if not n:
        return 0.0, 0.0
    p = passes / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return centre - half, centre + half


def run_cost(run_dir):
    path = Path(run_dir) / "calls.csv"
    if not path.exists():
        return None
    with path.open() as f:
        return round(sum(float(r.get("cost_usd") or 0) for r in csv.DictReader(f)), 4)


def records(run_dir):
    """One record per model, ladder and measured level of one run."""
    run_dir = Path(run_dir)
    meta = run_dir / "run.json"
    version = (
        json.loads(meta.read_text()).get("rules_version") if meta.exists() else None
    )
    cost = run_cost(run_dir)
    per_model = collections.defaultdict(list)
    for m, t, lv, ok in trials(run_dir):
        per_model[m].append((t, lv, ok))
    out = []
    for m in sorted(per_model):
        for taxonomy in LADDERS:
            for lv, ok, n in ladder(per_model[m], taxonomy):
                if not n:
                    continue
                low, high = wilson(ok, n)
                judged = taxonomy == "cognitive" and lv in JUDGED
                out.append(
                    {
                        "model": m,
                        "ladder": taxonomy,
                        "level": lv,
                        "trials": n,
                        "passes": ok,
                        "rate": round(ok / n, 4),
                        "wilson_low": round(low, 4),
                        "wilson_high": round(high, 4),
                        "passed": n >= MIN_TRIALS and ok / n >= PASS_RATE,
                        "graded_by": "judge" if judged else "script",
                        "judge_kappa": JUDGED[lv] if judged else None,
                        "rules_version": version,
                        "cost_usd": cost,
                    }
                )
    return out


def write_json(run_dir):
    path = Path(run_dir) / "ladder-scores.json"
    data = {
        "schema": "docs/reference/ladder-scores.schema.json",
        "schema_version": SCHEMA_VERSION,
        "run": str(run_dir),
        "pass_rule": f"{PASS_RATE:.0%} of {MIN_TRIALS} trials or more",
        "cost_usd_is": "the cost of the whole run, repeated on each record",
        "judge_kappa_source": KAPPA_SOURCE,
        "records": records(run_dir),
    }
    path.write_text(json.dumps(data, indent=2) + "\n")
    return path


def main(argv):
    argv = list(argv)
    as_json = "--json" in argv
    if as_json:
        argv.remove("--json")
    if not argv:
        sys.exit(__doc__)
    print(report(argv))
    if as_json:
        for d in argv:
            print(f"wrote {write_json(d)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
