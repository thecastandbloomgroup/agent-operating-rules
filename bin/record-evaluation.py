"""Write the record of the evaluation runs from the scores.csv of each run folder.
Usage: bin/record-evaluation.py [RESULTS_DIR]
  RESULTS_DIR  the folder with one subfolder per run (default tests/evaluation/results)
It rewrites tests/evaluation/evaluation-scores.csv, the cross-model summary and the
runs of tests/evaluation/evaluation-results.md, and the results of
docs/reference/evaluation.md. It calls no API. A run is recorded when a model of it
answers 5 prompts or more. Each other run is a check of the harness, and only its
name is listed. A run folder with combined-from.txt combines the runs that the file
names, one on each line. Those runs are named once, and their scores are not counted
twice. Run mdformat on the two Markdown files after it: task eval:record does.
"""

import csv
import importlib.util
import re
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
EVALUATION = ROOT / "tests" / "evaluation"
RESULTS_MD = EVALUATION / "evaluation-results.md"
SCORES_CSV = EVALUATION / "evaluation-scores.csv"
REFERENCE = ROOT / "docs" / "reference" / "evaluation.md"
CRITERIA = [f"R{n}" for n in range(1, 10)]
ORDER = ["C1", "C2", "K1", "K2", "X1", "X2", "H1", "H2", "U1", "U2", "T1", "T2", "T3"]
MIN_PROMPTS = 5
# scores.csv gives the T prompts the name of their section. The run template names their domain.
DOMAIN = {
    "T1": "Clear (worded Complex)",
    "T2": "Complex (worded Clear)",
    "T3": "Mixed",
}
# The versions before 0.3.0 were renamed (CHANGELOG.md, 0.3.0).
RENAMED = {"2.1.0": "0.1.0", "3.0.0": "0.2.0", "3.1.0": "0.2.1", "3.2.0": "0.2.2"}
# The rule of the rules file that each criterion tests (evaluation-tests.md, Section 3).
RULE = {
    "R1": "6.5, the domain of each action",
    "R2": "6.5, the domain of each action",
    "R3": "6.5, the action form of each domain",
    "R4": "6.5, the trade-off rules",
    "R5": "6.4, the test form of each task kind",
    "R6": "6.5, the domain of each action",
    "R7": "2, ask, assume, or proceed",
    "R8": "4.6, calibrated uncertainty",
    "R9": "the whole file",
}


def provider(model):
    return model.split("/")[0]


def sample(row):
    found = re.search(r"-s(\d+)\.md$", row["response_file"])
    return int(found.group(1)) if found else 1


def combined(folder):
    """The runs that another run combines, as {combined run: [source runs]}."""
    return {
        path.parent.name: sorted(set(path.read_text().split()))
        for path in Path(folder).glob("*/combined-from.txt")
    }


def read_runs(folder):
    """Each run folder with a scores.csv, as {run: rows}, newest date first.
    It leaves out each run that another run combines."""
    sources = {s for group in combined(folder).values() for s in group}
    runs = {}
    for path in sorted(Path(folder).glob("*/scores.csv"), reverse=True):
        if path.parent.name in sources:
            continue
        rows = [r for r in csv.DictReader(path.open()) if r["total"]]
        for r in rows:
            r["run"] = path.parent.name
            r["rules_version"] = RENAMED.get(r["rules_version"], r["rules_version"])
        if rows:
            runs[path.parent.name] = rows
    return dict(sorted(runs.items(), key=lambda kv: kv[1][0]["date"], reverse=True))


def recorded(rows):
    prompts = defaultdict(set)
    for r in rows:
        prompts[r["model"]].add(r["prompt_id"])
    return max(len(p) for p in prompts.values()) >= MIN_PROMPTS


def by_model(rows):
    models = defaultdict(list)
    for r in rows:
        models[r["model"]].append(r)
    return models


def same(r):
    return provider(r["grader"]) == provider(r["model"])


def lowest(rows):
    means = {
        c: mean(int(r[c]) for r in rows if r[c] != "")
        for c in CRITERIA
        if any(r[c] != "" for r in rows)
    }
    c = min(means, key=means.get)
    return c, means[c]


def pairs(rows):
    """The judgments of each answer, as {(prompt, sample): {"A": row, "B": row}}."""
    answers = defaultdict(dict)
    for r in rows:
        answers[(r["prompt_id"], sample(r))]["A" if same(r) else "B"] = r
    key = lambda k: (ORDER.index(k[0]) if k[0] in ORDER else len(ORDER), k[1])
    return dict(sorted(answers.items(), key=lambda kv: key(kv[0])))


def passes(rows, grader_a):
    judged = [r for r in rows if same(r) == grader_a]
    return f"{sum(r['pass'] == 'yes' for r in judged)} of {len(judged)}"


def gaps(rows):
    return sum(
        1
        for a in pairs(rows).values()
        if len(a) == 2 and abs(int(a["A"]["total"]) - int(a["B"]["total"])) > 3
    )


def summary(rows):
    c, m = lowest(rows)
    return [
        str(len(pairs(rows))),
        passes(rows, True),
        passes(rows, False),
        f"{mean(int(r['total']) for r in rows):.1f}",
        f"{c} ({m:.2f})",
        str(gaps(rows)),
    ]


def cell(text):
    return text.replace("|", "\\|").replace("\n", " ").strip()


def first_sentence(text):
    return cell(re.split(r"(?<=[.!?])\s", text.strip(), maxsplit=1)[0])


def table(header, rows):
    lines = ["| " + " | ".join(header) + " |", "|" + " --- |" * len(header)]
    lines += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(lines)


def clean(path, checker):
    """True when the checker finds no banned word and no dash in the response."""
    report = checker.test(path)
    return report["banned_total"] == 0 and not report["dashes"]


def both(answer, field):
    """The field of grader A and of grader B, as "A / B"."""
    return " / ".join(answer[k][field] if k in answer else "none" for k in "AB")


def block(run, model, rows, checker, folder):
    answers = pairs(rows)
    several = any(s > 1 for _, s in answers)
    graders = {
        k: next((r["grader"] for r in rows if same(r) == (k == "A")), "none")
        for k in "AB"
    }
    lines = []
    for (prompt, s), a in answers.items():
        first = a.get("A") or a["B"]
        scores = [a["A"][c] or "n/a" for c in CRITERIA] if "A" in a else ["none"] * 9
        totals = [
            f"{a[k]['total']}/{a[k]['available']}" if k in a else "none" for k in "AB"
        ]
        lines.append(
            [
                f"{prompt} s{s}" if several else prompt,
                DOMAIN.get(prompt, first["domain"]),
            ]
            + [*scores, *totals]
            + [both(a, "gates_passed"), both(a, "pass")]
            + [first_sentence(first["main_defect"])]
        )
    files = {Path(folder) / run / r["response_file"] for r in rows}
    found = [f for f in files if f.exists()]
    c, m = lowest(rows)
    return "\n\n".join(
        [
            f"### Run `{run}`: `{model}`",
            (
                f"Rules version: {rows[0]['rules_version']}. Date: {rows[0]['date']}. "
                f"Grader A, same provider: `{graders['A']}`. "
                f"Grader B, other provider: `{graders['B']}`. "
                f"Responses: `results/{run}/responses/`."
            ),
            table(
                [
                    "Prompt",
                    "Domain",
                    *(f"A: {c}" for c in CRITERIA),
                    "A total",
                    "B total",
                ]
                + ["Gates A / B", "Pass A / B", "Main defect"],
                lines,
            ),
            (
                f"Lowest-scoring criterion: {c}, mean {m:.2f}.\n"
                f"Rule it points to: Section {RULE[c]}.\n"
                "Change intended: see the write-ups named at the start of Runs."
            ),
            f"Responses with no banned word and no dash: {sum(clean(f, checker) for f in found)} of {len(found)}.",
        ]
    )


SUMMARY_HEADER = [
    "Run",
    "Model",
    "Rules version",
    "Answers",
    "Pass, grader A",
    "Pass, grader B",
]
SUMMARY_HEADER += ["Mean score", "Lowest criterion", "Grader gap over 3 (count)"]


def results_md(text, runs, checker, folder):
    kept = {run: rows for run, rows in runs.items() if recorded(rows)}
    checks = [run for run in runs if run not in kept]
    rows = [
        [f"`{run}`", f"`{model}`", group[0]["rules_version"], *summary(group)]
        for run, all_rows in kept.items()
        for model, group in by_model(all_rows).items()
    ]
    head, rest = text.split("## Cross-model summary", 1)
    template = (
        "## Run template" + rest.split("## Run template", 1)[1].split("## Runs", 1)[0]
    )
    blocks = [
        block(run, model, group, checker, folder)
        for run, all_rows in kept.items()
        for model, group in by_model(all_rows).items()
    ]
    return (
        head
        + "## Cross-model summary\n\n"
        + "`bin/record-evaluation.py` writes this table and the runs from the scores.csv of each run. "
        + "One row for each model of each run. Grader A is the judge of the same provider, and grader B is the judge of another provider. "
        + "Mean score is over all judgments of both graders. Each answer has 16 or 18 available points.\n\n"
        + table(SUMMARY_HEADER, rows)
        + "\n\n"
        + template
        + "## Runs\n\n"
        + "Newest date first. The write-ups of the runs are in `results/`: the learnings of 2026-10-29, the assessment of 2026-10-30, and the probe results of 2026-10-30. "
        + "The runs at rules version 0.2.2 used a checker that missed the references of many answers, and C1, C2, K1 and K2 had no attached files. "
        + "So their scores are lower than the same answers would get now.\n\n"
        + f"Checks of the harness, with fewer than {MIN_PROMPTS} prompts for each model: "
        + ", ".join(f"`{run}`" for run in checks)
        + ".\n\n"
        + "".join(
            f"`{run}` combines the partial runs "
            + " and ".join(f"`{s}`" for s in sources)
            + ". So those runs have no rows of their own.\n\n"
            for run, sources in combined(folder).items()
        )
        + "\n\n".join(blocks)
        + "\n"
    )


def reference_md(text, runs):
    full = [
        r
        for rows in runs.values()
        if len({x["prompt_id"] for x in rows}) == len(ORDER)
        for r in rows
    ]
    rows = []
    for model, group in by_model(full).items():
        c, m = lowest(group)
        rows.append(
            [
                f"`{model}`",
                str(len({r["run"] for r in group})),
                str(len({(r["run"], r["prompt_id"], sample(r)) for r in group})),
                passes(group, True),
                passes(group, False),
                f"{mean(int(r['total']) for r in group):.1f}",
                f"{c} ({m:.2f})",
            ]
        )
    c, m = lowest(full)
    head = text.split("## Results", 1)[0]
    return (
        head
        + "## Results\n\n"
        + "`bin/record-evaluation.py` writes this table from the runs of all 13 prompts. "
        + "Each run of `evaluation-results.md` has its own row and table there. "
        + "Grader A is the judge of the same provider, and grader B is the judge of another provider.\n\n"
        + table(
            [
                "Model",
                "Runs",
                "Answers",
                "Pass, grader A",
                "Pass, grader B",
                "Mean score",
                "Lowest criterion",
            ],
            rows,
        )
        + f"\n\nThe criterion with the lowest mean across all models is {c} ({m:.2f}). "
        + f"It names the rule to fix first: Section {RULE[c]}.\n"
    )


def scores_csv(runs, path):
    with path.open("w", newline="") as out:
        fields = list(next(iter(runs.values()))[0])
        fields = [f for f in fields if f != "run"]
        writer = csv.DictWriter(out, fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        for run, rows in runs.items():
            if recorded(rows):
                for r in rows:
                    writer.writerow(
                        {**r, "response_file": f"results/{run}/{r['response_file']}"}
                    )


def load_checker():
    spec = importlib.util.spec_from_file_location(
        "checker", ROOT / "bin" / "deterministic-tests.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else EVALUATION / "results"
    runs = read_runs(folder)
    if not runs:
        sys.exit(f"no scores.csv under {folder}")
    scores_csv(runs, SCORES_CSV)
    RESULTS_MD.write_text(
        results_md(RESULTS_MD.read_text(), runs, load_checker(), folder)
    )
    REFERENCE.write_text(reference_md(REFERENCE.read_text(), runs))
