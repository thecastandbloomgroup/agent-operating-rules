"""Print each relative link in Markdown files to a file that does not exist.
Usage: check-links.py PATH...
  PATH  a Markdown file, or a folder whose .md files are read recursively
It exits with 1 when it prints a link.
"""

import re
import sys
from pathlib import Path

# The target of [text](target), up to a # anchor. A link to an anchor only has no target.
LINK = re.compile(r"\]\(([^)#\s]+)")


def pages(paths):
    for root in map(Path, paths):
        yield from [root] if root.is_file() else sorted(root.rglob("*.md"))


def broken(page):
    return [
        target
        for target in LINK.findall(page.read_text())
        if "://" not in target and not (page.parent / target).exists()
    ]


if __name__ == "__main__":
    bad = [
        f"{page}: {target}" for page in pages(sys.argv[1:]) for target in broken(page)
    ]
    for line in bad:
        print(line)
    sys.exit(1 if bad else 0)
