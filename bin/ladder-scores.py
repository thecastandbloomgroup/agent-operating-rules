"""Score each model on the Bloom ladders of the evaluation design, from the checks of runs.
Usage: bin/ladder-scores.py RUN_DIR [RUN_DIR ...]
It reads RUN_DIR/script-checks.csv (bin/script-checks.py) and, when present,
RUN_DIR/action-checks.csv and RUN_DIR/action-checks-argon.csv (bin/judge-actions.py)
and RUN_DIR/tool-checks.csv (bin/check-psychomotor.py), the psychomotor trials.
Evaluate counts the self-test lines that the script checks, except the word counts.
Each check counts as one trial of one level (MAP). A level is mastered at 80% of 20
trials or more. The score of a taxonomy is (L + p) / N, where L is the highest level
mastered with every measured level below it mastered, p is the rate of the next
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
MASTERY, MIN_TRIALS, TOLERANCE = 0.8, 20, 0.05
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
    mastered = 0
    for _, ok, n in measured:
        if n >= MIN_TRIALS and ok / n >= MASTERY:
            mastered += 1
        else:
            break
    nxt = (
        measured[mastered][1] / measured[mastered][2]
        if mastered < len(measured)
        else 0.0
    )
    return mastered, nxt, len(measured), (mastered + nxt) / len(measured), True


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
            "* fewer than 20 trials, so the level cannot count as mastered.",
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


def main(argv):
    if not argv:
        sys.exit(__doc__)
    print(report(argv))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
