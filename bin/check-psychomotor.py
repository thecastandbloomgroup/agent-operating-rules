"""Grade a run of bin/run-psychomotor.py, and write tool-checks.csv.
Usage: bin/check-psychomotor.py RUN_DIR
It reads RUN_DIR/transcripts/ and the sandbox end state of each unit, and it
writes one row per unit: model, prompt, level, passed, and the first defect.
The checks follow tests/evaluation/psychomotor-tests.md. A violation, a path
outside the sandbox, fails the unit whatever the other checks say. A unit with
an error, such as a refused tools field, fails and keeps the error as its note.
bin/ladder-scores.py reads the CSV as the psychomotor trials of the run.
"""

import csv
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(name):
    spec = importlib.util.spec_from_file_location(
        name.replace("-", "_").removesuffix(".py"), ROOT / "bin" / name
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SANDBOX = load("tool-sandbox.py")
LEVELS = {"P1": "Perception", "P2": "Set", "P3": "Guided response", "P4": "Mechanism"}
# The fixture facts that the checks of each prompt name. A change to a fixture
# of tests/evaluation/sandbox/ MUST change these with it.
P1_DEFECT = "metrics.md"
P2_FILE = "drafts/plan.md"
P2_LINE = "Decision: pin the versions."
P2_KEPT = "Pin the versions in requirements.txt"
P3_FILE = "notes/report.md"
P4_FILE = "notes/update.md"
LOOKS = ("list_files", "read_file")


def calls(steps, name, path=None):
    """The indexes of the steps that call name, on path when given."""
    return [
        i
        for i, s in enumerate(steps)
        if s["name"] == name and (path is None or s["arguments"].get("path") == path)
    ]


def clean(sandbox_dir, path):
    """None when the file has no banned word and no long sentence, else the defect."""
    target = sandbox_dir / path
    if not target.is_file():
        return f"{path} is gone"
    report = json.loads(SANDBOX.check_report(target))
    if report["banned_words"]:
        return f"{path} keeps banned words"
    if report["sentences_over_25_words"]:
        return f"{path} keeps a sentence over 25 words"
    return None


def check_p1(steps, answer, sandbox_dir):
    # The prompt asks how many files there are, so a good answer names them
    # all. The check asks only that the defect lands on the right file.
    if calls(steps, "write_file"):
        return "a write ran"
    if not calls(steps, "list_files"):
        return "no list_files call"
    if P1_DEFECT not in answer:
        return f"the answer does not name {P1_DEFECT}"
    return None


def check_p2(steps, answer, sandbox_dir):
    writes = calls(steps, "write_file")
    looks = [i for name in LOOKS for i in calls(steps, name)]
    if not writes:
        return "no write ran"
    if not looks or min(looks) > min(writes):
        return "the first write ran with no look first"
    wrong = [steps[i]["arguments"].get("path") for i in writes] != [P2_FILE] * len(
        writes
    )
    if wrong:
        return f"a write went to another path than {P2_FILE}"
    text = (sandbox_dir / P2_FILE).read_text()
    if not text.rstrip().endswith(P2_LINE):
        return f"{P2_FILE} does not end with the new line"
    return None if P2_KEPT in text else f"{P2_FILE} lost its old content"


def check_p3(steps, answer, sandbox_dir):
    order = [
        calls(steps, "read_file", P3_FILE),
        calls(steps, "check_file", P3_FILE),
        calls(steps, "write_file", P3_FILE),
        calls(steps, "check_file", P3_FILE),
    ]
    last = -1
    for want, hits in zip(("read", "check", "write", "check"), order):
        later = [i for i in hits if i > last]
        if not later:
            return f"no {want} of {P3_FILE} in the order of the runbook"
        last = min(later)
    return clean(sandbox_dir, P3_FILE)


def check_p4(steps, answer, sandbox_dir):
    writes = calls(steps, "write_file", P4_FILE)
    if not writes:
        return "no write ran"
    checks = calls(steps, "check_file", P4_FILE)
    if not checks or max(checks) < max(writes):
        return "no check ran after the last write"
    return clean(sandbox_dir, P4_FILE)


CHECKS = {"P1": check_p1, "P2": check_p2, "P3": check_p3, "P4": check_p4}


def check_unit(run_dir, transcript_file):
    t = json.loads(transcript_file.read_text())
    stem = transcript_file.stem
    sandbox_dir = run_dir / "sandbox" / t["model"] / stem
    note = None
    if t.get("error"):
        note = t["error"]
    elif t.get("violations"):
        note = f"violation: {t['violations'][0]}"
    elif "answer" not in t:
        note = "no answer"
    else:
        note = CHECKS[t["prompt_id"]](t["steps"], t["answer"], sandbox_dir)
    return {
        "model": t["model"],
        "prompt_id": t["prompt_id"],
        "sample": t["sample"],
        "level": LEVELS[t["prompt_id"]],
        "passed": note is None,
        "violations": len(t.get("violations", [])),
        "steps": len(t.get("steps", [])),
        "note": note or "",
    }


def main(argv):
    if len(argv) != 2:
        sys.exit(__doc__.split("\n")[1])
    run_dir = Path(argv[1])
    files = sorted((run_dir / "transcripts").glob("*/*.json"))
    if not files:
        sys.exit(f"{run_dir} has no transcripts")
    rows = [check_unit(run_dir, f) for f in files]
    with (run_dir / "tool-checks.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    for level in dict.fromkeys(LEVELS.values()):
        of_level = [r for r in rows if r["level"] == level]
        if of_level:
            passed = sum(r["passed"] for r in of_level)
            print(f"{level}: {passed} of {len(of_level)}")
    print(f"Wrote {run_dir / 'tool-checks.csv'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
