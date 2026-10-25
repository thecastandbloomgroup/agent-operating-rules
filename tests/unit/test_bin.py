"""Unit tests of the scripts in bin/. Run: python3 -m unittest discover -s tests/unit"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

BIN = Path(__file__).resolve().parents[2] / "bin"


def run(script, *args):
    return subprocess.run(
        [sys.executable, str(BIN / script), *args],
        capture_output=True,
        text=True,
        check=False,
    )


class CheckLinks(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.dir = Path(folder.name)
        (self.dir / "target.md").write_text("# Target\n")

    def test_prints_nothing_when_every_link_has_a_file(self):
        (self.dir / "page.md").write_text("See [the target](target.md).\n")
        result = run("check-links.py", str(self.dir))
        self.assertEqual((result.returncode, result.stdout), (0, ""))

    def test_names_each_link_with_no_file(self):
        (self.dir / "page.md").write_text("See [a lost page](lost.md).\n")
        result = run("check-links.py", str(self.dir))
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, f"{self.dir / 'page.md'}: lost.md\n")


class DeterministicTests(unittest.TestCase):
    def report(self, text):
        with tempfile.TemporaryDirectory() as folder:
            page = Path(folder) / "page.md"
            page.write_text(text)
            result = run("deterministic-tests.py", "--check", str(page))
        return result.returncode, json.loads(result.stdout)

    def test_no_grade_for_a_page_with_no_prose(self):
        code, report = self.report(
            "# Files\n\n| File | Job |\n| - | - |\n| a.md | b |\n"
        )
        self.assertEqual(code, 0)
        self.assertIsNone(report["fk_grade"])
        self.assertIsNone(report["flesch_ease"])
        self.assertEqual(report["failures"], [])

    def test_grade_for_a_page_with_prose(self):
        code, report = self.report("The cat sat on the mat. It slept there.\n")
        self.assertEqual(code, 0)
        self.assertIsInstance(report["fk_grade"], float)
        self.assertIsInstance(report["flesch_ease"], float)

    def test_names_an_acronym_that_has_an_alias(self):
        code, report = self.report("Write the BLUF first. It holds the answer.\n")
        self.assertEqual(code, 1)
        self.assertIn("banned words (4.2.3, 4.2.6, 4.4)", report["failures"])
        hits = report["banned"]["Acronyms with an alias (4.2.6)"]
        self.assertEqual([word for word, _ in hits], ["bluf"])

    def test_no_finding_for_an_acronym_in_backticks(self):
        code, report = self.report("The alias of `BLUF` is Headline.\n")
        self.assertEqual(code, 0)
        self.assertEqual(report["banned_total"], 0)


if __name__ == "__main__":
    unittest.main()
