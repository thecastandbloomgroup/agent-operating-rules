"""Score the answers of runs with the script checks of item-labels.yaml: STRUCTURE,
LANGUAGE, SELFTEST, and the domain label of each action in End. No judge, no API call.
Usage: bin/script-checks.py RUN_DIR [RUN_DIR ...]
Each run folder needs run.json (written by bin/run-evaluation.py) and responses/.
It writes RUN_DIR/script-checks.csv for each run, and prints one table per run and,
for two runs, the difference of each rate with its 95% interval.
"""

import csv
import importlib.util
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ("Clear", "Complicated", "Complex", "Chaotic", "Confused")
BRIEF = ("Background", "Relevance", "Information", "End")
# The rates that the tables report, in order, with their columns of script-checks.csv.
RATES = {
    "STRUCTURE": "structure",
    "LANGUAGE": "language",
    "no long sentence": "no_long_sentence",
    "no first person outside End": "no_first_person",
    "every action labelled": "all_labelled",
    "every label with a reason": "all_reasoned",
    "self-test counts right": "selftest_right",
}


def load_checker():
    spec = importlib.util.spec_from_file_location(
        "checker", ROOT / "bin" / "deterministic-tests.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CHECKER = load_checker()


HEADINGS = ("Headline", *BRIEF, "Follow-up", "Self-test")
# A heading is a line that is only one of the seven names of Section 3: with or
# without Markdown hashes, bold, or a colon. The rules fix the names, not the syntax.
HEADING = re.compile(
    r"(?im)^[ \t]*#{0,6}[ \t]*\**[ \t]*("
    + "|".join(HEADINGS)
    + r")[ \t]*\**:?\**[ \t]*$"
)


def headings(text):
    """The heading lines of an answer that are not inside a code block."""
    fences = [m.start() for m in re.finditer(r"(?m)^[ \t]*```", text)]
    return [
        m
        for m in HEADING.finditer(text)
        if sum(1 for f in fences if f < m.start()) % 2 == 0
    ]


def sections(text):
    """The sections of an answer under the seven heading names, in order, with their bodies.
    A Self-test block with no heading of its own starts a Self-test section."""
    marks = headings(text)
    if not any(m.group(1).lower() == "self-test" for m in marks):
        text = re.sub(r"(?m)^(```[a-z]*\n)(?=Self-test\s*\n)", r"Self-test\n\1", text)
        marks = headings(text)
    names = {h.lower(): h for h in HEADINGS}
    return [
        (
            names[m.group(1).lower()],
            text[m.end() : marks[i + 1].start() if i + 1 < len(marks) else len(text)],
        )
        for i, m in enumerate(marks)
    ]


def section(text, name):
    for heading, body in sections(text):
        if heading.lower() == name.lower():
            return body
    return ""


def structure(text):
    names = [h for h, _ in sections(text)]
    brief = [n for n in names if n in BRIEF]
    follow = names.index("Follow-up") if "Follow-up" in names else None
    end = section(text, "End").strip()
    return {
        "headline_first": bool(names) and names[0] == "Headline",
        "brief_in_order": brief == list(BRIEF)
        and (follow is None or follow > names.index("End")),
        "end_begins": end.startswith("I recommend that we"),
        "selftest_last": bool(names) and names[-1] == "Self-test",
    }


# A3 of tests 1.7 asks for no headings. Its answer passes STRUCTURE by these checks.
NO_HEADINGS = {"A3"}


def plain_structure(text):
    """The structure checks of an answer that the prompt asks to write with no headings."""
    fences = list(re.finditer(r"(?ms)^```[a-z]*\n(.*?)^```", text))
    last = fences[-1] if fences else None
    return {
        "no_heading": not headings(text) and not re.search(r"(?m)^#{1,6}\s", text),
        "end_begins": bool(re.search(r"(?m)^I recommend that we", text)),
        "selftest_last": bool(last)
        and last.group(1).startswith("Self-test")
        and not text[last.end() :].strip(),
    }


def with_headings(text):
    """Mark the parts of an answer that has no headings, so that the other checks can
    read it: Information up to the recommendation, End up to the Self-test block."""
    text = re.sub(r"(?m)^(?=I recommend that we)", "## End\n", text, count=1)
    return "## Information\n" + text


def actions(end):
    """The top-level numbered actions of End, each with its text up to the next one.
    An action can also start as a heading, as in "### 1. Keep summaries as drafts"."""
    starts = list(re.finditer(r"(?m)^(?:#{1,6}[ \t]*)?\d+\.\s", end))
    return [
        end[m.start() : starts[i + 1].start() if i + 1 < len(starts) else len(end)]
        for i, m in enumerate(starts)
    ]


def reason(rest):
    """Whether the text after a domain name gives a reason: the rest of its sentence,
    or the next sentence on the line. A next field such as "Kind: deterministic."
    or a dependency clause ("Step 3 MUST NOT start") is not a reason."""
    first, *after = re.split(r"(?<=[.!?])\s+", rest.strip(), maxsplit=1)
    if len(re.findall(r"[A-Za-z]+", first)) >= 3:
        return True
    nxt = after[0] if after else ""
    return bool(nxt) and not re.match(r"(?:[A-Z]\w*(?: \w+)?:|Step \d)", nxt)


def label(action):
    """The domain of an action, and whether a reason follows. The domain is named on a
    Cynefin or Domain line, first in the action, as in "1. Clear, because ...", or in
    bold, as in "**Deterministic; Clear**, because ..."."""
    names = "|".join(DOMAINS)
    # A label is not followed by a lowercase word, so "**Clear the cache.**" is a title.
    m = re.match(
        r"\s*(?:#{1,6}\s*)?\d+\.\s+\**(" + names + r")\b(?!\s+[a-z])\**(.*)", action
    )
    if m:
        return m.group(1), reason(m.group(2))
    for line in action.split("\n"):
        m = re.search(
            r"\b(?:Cynefin|Domain)\b\W*(?:domain\W*)?(" + names + r")\b(.*)", line
        )
        if m:
            return m.group(1), reason(m.group(2))
    for line in action.split("\n"):
        m = re.search(
            r"\*\*[^*\n]*\b(" + names + r")\b(?!\s+[a-z])[^*\n]*\*\*(.*)", line
        )
        if m:
            return m.group(1), reason(m.group(2))
    return None, False


def prose(text):
    """The text with code, inline code, and quoted strings removed."""
    text = re.sub(r"(?s)```.*?```", "", text)
    text = re.sub(r"`[^`]*`", "", text)
    return re.sub(r"\"[^\"\n]*\"|“[^”\n]*”", "", text)


def first_person(text):
    """Each first-person singular word outside End and the Self-test."""
    kept = [
        body for heading, body in sections(text) if heading not in ("End", "Self-test")
    ]
    words = re.findall(r"\b(?:I|me|my|mine)\b", prose("\n".join(kept)))
    return len(words)


def long_sentences(text):
    """Sentences over 25 words, or over 20 words in End, as section 4.1 sets."""
    count = 0
    for heading, body in sections(text):
        if heading == "Self-test":
            continue
        limit = 20 if heading == "End" else 25
        count += sum(
            1
            for _, s in CHECKER.sentences(body)
            if len(s.split()) > limit and not CHECKER.is_list_sentence(s)
        )
    return count


def selftest(text):
    """The lines of the Self-test block, as {name: value}."""
    body = section(text, "Self-test")
    m = re.search(r"(?s)```[a-z]*\n(.*?)```", body)
    lines = (m.group(1) if m else body).split("\n")
    out = {}
    for line in lines:
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def number(value):
    m = re.match(r"\s*(\d+)", value or "")
    return int(m.group(1)) if m else None


def selftest_right(reported, actual):
    """Each count line of the self-test that the answer has, compared with the script."""
    checks = {
        "Dashes (em or en)": actual["dashes"],
        "Banned words found": actual["banned"],
        "Self-mention outside End": actual["first_person"],
    }
    results = {
        k: number(reported.get(k)) == v for k, v in checks.items() if k in reported
    }
    if "Longest sentence" in reported:
        n = number(reported["Longest sentence"])
        results["Longest sentence"] = n is not None and abs(n - actual["longest"]) <= 2
    over = [k for k in reported if k.startswith("Sentences over")]
    if over:
        results[over[0]] = number(reported[over[0]]) == actual["long"]
    key = "Actions in End with a Cynefin domain label"
    if key in reported:
        m = re.match(r"\s*(\d+)\s+of\s+(\d+)", reported[key])
        results[key] = bool(m) and (int(m.group(1)), int(m.group(2))) == (
            actual["labelled"],
            actual["actions"],
        )
    return results


def score(path):
    """The script checks of one answer file."""
    text = Path(path).read_text()
    text = text.split("\n", 2)[2] if text.count("\n") >= 2 else text  # the header line
    plain = Path(path).stem.split("-s")[0] in NO_HEADINGS
    struct = plain_structure(text) if plain else structure(text)
    # Every row has every structure column, blank where it does not apply.
    columns = {k: "" for k in ("headline_first", "brief_in_order", "no_heading")}
    if plain:
        text = with_headings(text)
    report = CHECKER.test(path)
    banned = sum(
        len(v) for k, v in report["banned"].items() if not k.startswith("Self-mention")
    )
    acts = actions(section(text, "End"))
    labels = [label(a) for a in acts]
    longest = max(
        (
            len(s.split())
            for h, b in sections(text)
            if h != "Self-test"
            for _, s in CHECKER.sentences(b)
        ),
        default=0,
    )
    actual = {
        "dashes": len(report["dashes"]),
        "banned": banned,
        "first_person": first_person(text),
        "long": long_sentences(text),
        "longest": longest,
        "actions": len(acts),
        "labelled": sum(1 for d, _ in labels if d),
    }
    lines = selftest_right(selftest(text), actual)
    row = {
        **actual,
        "reasoned": sum(1 for d, r in labels if d and r),
        **columns,
        **struct,
        "structure": all(struct.values()),
        "no_long_sentence": actual["long"] == 0,
        "no_first_person": actual["first_person"] == 0,
        "selftest_lines": len(lines),
        "selftest_wrong": ";".join(k for k, v in lines.items() if not v),
        "selftest_right": bool(lines) and all(lines.values()),
    }
    row["language"] = (
        actual["dashes"] == 0
        and banned == 0
        and row["no_long_sentence"]
        and row["no_first_person"]
    )
    row["all_labelled"] = bool(acts) and actual["labelled"] == len(acts)
    row["all_reasoned"] = bool(acts) and row["reasoned"] == len(acts)
    return row


def score_run(run_dir):
    run_dir = Path(run_dir)
    meta = json.loads((run_dir / "run.json").read_text())
    rows = []
    for path in sorted((run_dir / "responses").glob("*/*.md")):
        rows.append(
            {
                "rules_version": meta["rules_version"],
                "model": path.parent.name,
                "prompt_id": path.stem.split("-s")[0],
                "file": str(path.relative_to(run_dir)),
                **score(path),
            }
        )
    if rows:
        with (run_dir / "script-checks.csv").open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    return meta, rows


def rate(rows, column):
    n = len(rows)
    return (sum(1 for r in rows if r[column]) / n if n else 0.0), n


def difference(a, b, column):
    """The difference of two rates, b minus a, with a 95% normal interval."""
    pa, na = rate(a, column)
    pb, nb = rate(b, column)
    if not na or not nb:
        return 0.0, 0.0
    se = math.sqrt(pa * (1 - pa) / na + pb * (1 - pb) / nb)
    return pb - pa, 1.96 * se


def table(meta, rows):
    models = sorted({r["model"] for r in rows})
    head = "| Rate | All | " + " | ".join(models) + " |"
    out = [f"Rules {meta['rules_version']}: {len(rows)} answers", "", head]
    out.append("| --- " * (len(models) + 2) + "|")
    for name, column in RATES.items():
        cells = [f"{rate(rows, column)[0]:.0%}"]
        for m in models:
            cells.append(f"{rate([r for r in rows if r['model'] == m], column)[0]:.0%}")
        out.append(f"| {name} | " + " | ".join(cells) + " |")
    return "\n".join(out)


def compare(runs):
    (ma, a), (mb, b) = runs
    out = [
        f"Rules {ma['rules_version']} against {mb['rules_version']}",
        "",
        f"| Rate | {ma['rules_version']} | {mb['rules_version']} | Difference (95% interval) |",
        "| --- | --- | --- | --- |",
    ]
    for name, column in RATES.items():
        d, half = difference(a, b, column)
        out.append(
            f"| {name} | {rate(a, column)[0]:.0%} | {rate(b, column)[0]:.0%} | "
            f"{d:+.0%} ({d - half:+.0%} to {d + half:+.0%}) |"
        )
    return "\n".join(out)


def main(argv):
    if not argv:
        sys.exit(__doc__)
    runs = [score_run(d) for d in argv]
    for meta, rows in runs:
        print(table(meta, rows) + "\n")
    if len(runs) == 2:
        print(compare(runs))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
