"""Print each commit whose subject is not a Conventional Commit 1.0.0
(https://www.conventionalcommits.org/en/v1.0.0/).
Usage: check-commits.py [RANGE]
  RANGE  the commits for git log to read (default origin/main..HEAD)
It exits with 1 when it prints a commit.
"""

import re
import subprocess
import sys

# The types of docs/how-to/release-a-version.md. Each maps to a section of CHANGELOG.md.
TYPES = "feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert"
SUBJECT = re.compile(rf"^(?:{TYPES})(?:\([a-z0-9./-]+\))?!?: \S")


def conventional(subject):
    return bool(SUBJECT.match(subject))


def subjects(revisions):
    log = subprocess.run(
        ["git", "log", "--format=%h %s", revisions],
        capture_output=True,
        text=True,
        check=True,
    )
    return [line.split(" ", 1) for line in log.stdout.splitlines()]


if __name__ == "__main__":
    revisions = sys.argv[1] if len(sys.argv) > 1 else "origin/main..HEAD"
    bad = [f"{sha} {s}" for sha, s in subjects(revisions) if not conventional(s)]
    if bad:
        print("\n".join(bad))
    sys.exit(1 if bad else 0)
