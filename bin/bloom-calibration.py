"""Check model labels of Bloom's taxonomy against labels by people.
The data is the four human-labelled sets of question datasets in the AIED 2026
repository of Rasoulkhani et al. The repository is MIT, but the source datasets
state no licence. So the questions stay in a scratch folder and are never committed.
Usage: bin/bloom-calibration.py sample DIR [--per-level 34] [--seed 11]
       bin/bloom-calibration.py score DIR NAME [NAME ...]
sample downloads the four files at a pinned commit into DIR/raw, and writes
DIR/sheet.csv (id, question) for the labellers and DIR/gold-DO-NOT-READ.csv (id,
source, level). A labeller writes DIR/labels-NAME.csv (id, level). score prints
the agreement of each NAME with the people, and of two NAMEs with each other.
"""

import argparse
import collections
import csv
import random
import sys
import urllib.request
from pathlib import Path

REPO = "https://gitlab.com/zrasoulkhani/bloom-classification-aied2026/-/raw"
COMMIT = "786e25cc6daed10ebd1c9f511158decfde07a687"
FILES = [
    "Gani_2023_collected-dataset-1200_revised.csv",
    "Mohammed-and-Omar_2020_126_revised.csv",
    "Sangodiah_2017_415_revised.csv",
    "yahya-2012_revised.csv",
]
LEVELS = ["Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"]
BAND = {
    "Remember": "lower",
    "Understand": "lower",
    "Apply": "middle",
    "Analyze": "middle",
    "Evaluate": "higher",
    "Create": "higher",
}


def sample(folder, per_level, seed):
    raw = folder / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    rows = []
    for name in FILES:
        path = raw / name
        if not path.exists():
            urllib.request.urlretrieve(f"{REPO}/{COMMIT}/data/{name}", path)
        source = name.split("_")[0].split("-")[0]
        with path.open(encoding="utf-8", errors="replace") as f:
            for r in csv.DictReader(f):
                question, level = " ".join(r["QUESTION"].split()), r["BT LEVEL"].strip()
                if question and level in LEVELS:
                    rows.append((source, question, level))
    rng = random.Random(seed)
    picked = []
    for level in LEVELS:
        group = [r for r in rows if r[2] == level]
        rng.shuffle(group)
        picked += group[:per_level]
    rng.shuffle(picked)
    with (folder / "sheet.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "question"])
        writer.writerows([i, q] for i, (_, q, _) in enumerate(picked, 1))
    with (folder / "gold-DO-NOT-READ.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "source", "level"])
        writer.writerows([i, s, lv] for i, (s, _, lv) in enumerate(picked, 1))
    print(f"{len(picked)} questions from {len(rows)}")


def read(path):
    with path.open() as f:
        return {r["id"]: r["level"].strip().capitalize() for r in csv.DictReader(f)}


def kappa(x, y, categories):
    n = len(x)
    observed = sum(a == b for a, b in zip(x, y)) / n
    chance = sum((x.count(c) / n) * (y.count(c) / n) for c in categories)
    return observed, (observed - chance) / (1 - chance)


def agreement(a, b):
    """Exact agreement, kappa, within one level, and kappa on three bands."""
    ids = [i for i in b if i in a]
    x, y = [a[i] for i in ids], [b[i] for i in ids]
    exact, k = kappa(x, y, LEVELS)
    near = sum(
        a in LEVELS and abs(LEVELS.index(a) - LEVELS.index(b)) <= 1
        for a, b in zip(x, y)
    ) / len(ids)
    _, bands = kappa(
        [BAND.get(v, v) for v in x], [BAND.get(v, v) for v in y], set(BAND.values())
    )
    return {
        "n": len(ids),
        "exact": exact,
        "kappa": k,
        "within_one": near,
        "bands": bands,
    }


def confusion(labels, gold):
    """Rows: the level of the people. Columns: the level of the labeller."""
    counts = collections.Counter((gold[i], labels.get(i)) for i in gold)
    head = "| People \\ model | " + " | ".join(LEVELS) + " |"
    lines = [head, "| --- " * (len(LEVELS) + 1) + "|"]
    for g in LEVELS:
        lines.append(
            f"| {g} | " + " | ".join(str(counts[(g, m)]) for m in LEVELS) + " |"
        )
    return "\n".join(lines)


def score(folder, names):
    with (folder / "gold-DO-NOT-READ.csv").open() as f:
        gold = {r["id"]: r["level"] for r in csv.DictReader(f)}
    labels = {n: read(folder / f"labels-{n}.csv") for n in names}
    for n, lab in labels.items():
        r = agreement(lab, gold)
        print(
            f"{n} against people: n={r['n']}, exact {r['exact']:.0%}, kappa {r['kappa']:.2f}, "
            f"within one level {r['within_one']:.0%}, kappa on three bands {r['bands']:.2f}"
        )
        print(confusion(lab, gold) + "\n")
    if len(labels) == 2:
        (a, la), (b, lb) = labels.items()
        r = agreement(la, lb)
        print(f"{a} against {b}: exact {r['exact']:.0%}, kappa {r['kappa']:.2f}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    s = sub.add_parser("sample")
    s.add_argument("dir")
    s.add_argument("--per-level", type=int, default=34)
    s.add_argument("--seed", type=int, default=11)
    c = sub.add_parser("score")
    c.add_argument("dir")
    c.add_argument("names", nargs="+")
    args = parser.parse_args()
    if args.command == "sample":
        sample(Path(args.dir), args.per_level, args.seed)
    else:
        score(Path(args.dir), args.names)
    return 0


if __name__ == "__main__":
    sys.exit(main())
