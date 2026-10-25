"""First-party conformity assessment: test a Markdown file against model-operating-rules.md.
Usage: bin/deterministic-tests.py FILE [--instructions] [--check]
  --instructions  treat all sentences as instructions: 20-word limit
  --check         add the failed tests to the report, and exit 1 when one fails
"""

import json
import re
import sys
from pathlib import Path


def load_words(path=None):
    """Read banned-words.txt into {category: [entries]}."""
    path = (
        path or Path(__file__).resolve().parent.parent / "sources" / "banned-words.txt"
    )
    cats, cur = {}, None
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("# "):
            continue
        if line.startswith("## "):
            cur = line[3:]
            cats[cur] = []
        elif cur:
            cats[cur].append(line.lower())
    return cats


WORDS = load_words()
NOMINAL = [
    r"\bmake a decision\b",
    r"\bperform an analysis\b",
    r"\bconduct a review\b",
    r"\bprovide a recommendation\b",
    r"\bgive consideration\b",
    r"\btake into consideration\b",
    r"\bmake an assumption\b",
    r"\bcarry out an assessment\b",
]
GERUND_NOUN = r"\b(testing|building|measuring|planning|writing|checking|running)\s+of\b"
PASSIVE = r"\b(is|are|was|were|be|been|being)\s+(\w+ed|\w+en|known|done|given|made|shown|written|read|sent|set|put|told|found|built|held|kept|left|lost|met|paid|said|seen|taken|thought)\b"
EXEMPT_PREFIX = ("```", "[", "|", "<", "A<n>")


def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    groups = re.findall(r"[aeiouy]+", w)
    return max(1, len(groups))


def readability(sents):
    """Grade the prose sentences only, so that table rows and code do not count as one long sentence.
    A page with no prose sentence has no grade."""
    if not sents:
        return None, None
    words = [w for s in sents for w in re.findall(r"[A-Za-z]+", s)]
    sents = len(sents)
    nw = max(1, len(words))
    syl = sum(syllables(w) for w in words)
    fk = 0.39 * nw / sents + 11.8 * syl / nw - 15.59
    ease = 206.835 - 1.015 * nw / sents - 84.6 * syl / nw
    return round(fk, 1), round(ease, 1)


def sentences(text):
    out = []
    in_code = False
    for ln, line in enumerate(text.split("\n"), 1):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code or not line.strip() or line.lstrip().startswith(EXEMPT_PREFIX):
            continue
        if line.startswith("#"):
            continue
        body = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", line)
        body = re.sub(r"\*\*(.+?)\*\*", r"\1", body)
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"(])", body):
            s = s.strip()
            if s:
                out.append((ln, s))
    return out


def is_list_sentence(s):
    return s.startswith("Examples:") or s.count(",") >= 5 or s.count("(") >= 3


def test(path, instructions=False):
    text = Path(path).read_text()
    body, _, refs = text.partition("## References")
    R = {}
    sents = sentences(body)
    limit = 20 if instructions else 25

    R["sentences"] = len(sents)
    R["words"] = len(body.split())

    long = [
        (ln, len(s.split()), s[:60])
        for ln, s in sents
        if len(s.split()) > limit and not is_list_sentence(s)
    ]
    R["long_sentences"] = long

    dashes = [
        (i, line[:60])
        for i, line in enumerate(text.split("\n"), 1)
        if "—" in line or "–" in line
    ]
    R["dashes"] = dashes

    low = body.lower()

    def hits(words):
        found = []
        for w in words:
            for m in re.finditer(r"\b" + re.escape(w) + r"\b", low):
                after = low[m.end() : m.end() + 10]
                before = low[max(0, m.start() - 2) : m.start()]
                if w == "very" and after.startswith((" likely", " unlikely")):
                    continue  # IPCC scale terms
                if (
                    '"' in before
                    or "`" in before
                    or "examples:" in low[max(0, m.start() - 250) : m.start()]
                ):
                    continue  # quoted counter-example
                if "(" in before:
                    continue
                ctx = body[max(0, m.start() - 40) : m.end() + 40].replace("\n", " ")
                found.append((w, ctx))
        return found

    R["banned"] = {cat: hits(words) for cat, words in WORDS.items()}
    R["banned_total"] = sum(len(v) for v in R["banned"].values())

    def unquoted(pattern):
        return [
            m.group(0)
            for m in re.finditer(pattern, low)
            if '"' not in low[max(0, m.start() - 2) : m.start()]
        ]

    R["nominalizations"] = [x for p in NOMINAL for x in unquoted(p)]
    R["gerund_nouns"] = unquoted(GERUND_NOUN)
    pas = []
    for ln, s in sents:
        for m in re.finditer(PASSIVE, s):
            pas.append((ln, m.group(0), s[:60]))
    R["passive_count"] = len(pas)
    R["passive_sample"] = pas[:8]

    R["fk_grade"], R["flesch_ease"] = readability([s for _, s in sents])

    # citations
    cites = [int(x) for x in re.findall(r"\[(\d+)\]", body)]
    order = list(dict.fromkeys(cites))
    R["citation_order_ok"] = order == list(range(1, len(order) + 1))
    R["citations_first_appearance"] = order
    multi = [
        (i, line[:60])
        for i, line in enumerate(body.split("\n"), 1)
        if len(re.findall(r"\[\d+\]", line)) > 1
    ]
    R["multi_citation_lines"] = multi
    entries = re.findall(r"(?m)^\[(\d+)\] (.+)$", refs)
    R["ref_entries"] = len(entries)
    R["refs_untagged"] = [
        n for n, e in entries if not re.search(r"\[(P|S|T|U)\]\s*$", e)
    ]
    R["refs_uncited"] = [int(n) for n, _ in entries if int(n) not in order]
    R["cites_unlisted"] = [n for n in order if str(n) not in dict(entries)]
    blank_sep = all(b.strip() == "" for b in re.findall(r"\]\s*\n(.*)\n\[\d+\]", refs))
    R["refs_blank_line_separated"] = blank_sep if entries else None
    return R


def failures(R):
    """Name each test of the report that fails. The passive voice is a count, not a failure (4.1.2)."""
    passes = {
        "long sentences (4.1.1)": not R["long_sentences"],
        "dashes (4.3.1)": not R["dashes"],
        "banned words (4.2.3, 4.2.6, 4.4)": R["banned_total"] == 0,
        "nominalizations (4.2.4)": not R["nominalizations"],
        "gerund nouns (4.1.6)": not R["gerund_nouns"],
        "Flesch-Kincaid grade over 10 (4.1.7)": R["fk_grade"] is None
        or R["fk_grade"] <= 10,
        "citations out of order (5.4.1)": R["citation_order_ok"],
        "more than one citation on a line (5.4.1)": not R["multi_citation_lines"],
        "no blank line between references (5.4.1)": R["refs_blank_line_separated"]
        is not False,
        "reference with no source-type tag (5.4.5)": not R["refs_untagged"],
        "reference never cited": not R["refs_uncited"],
        "citation with no reference": not R["cites_unlisted"],
    }
    return [name for name, ok in passes.items() if not ok]


if __name__ == "__main__":
    args = sys.argv[1:]
    path = next(a for a in args if not a.startswith("--"))
    report = test(path, "--instructions" in args)
    if "--check" in args:
        report["failures"] = failures(report)
    print(json.dumps(report, indent=1, ensure_ascii=False))
    sys.exit(1 if report.get("failures") else 0)
