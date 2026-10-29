"""Unit tests of the scripts in bin/. Run: python3 -m unittest discover -s tests/unit"""

import contextlib
import importlib.util
import io
import json
import re
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


def load(script):
    """Import a script of bin/, whose name has a hyphen, as a module."""
    spec = importlib.util.spec_from_file_location(
        script.replace("-", "_"), BIN / script
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


EVAL = load("run-evaluation.py")


class RunEvaluationPairs(unittest.TestCase):
    def setUp(self):
        self.cfg = json.loads((BIN.parent / "tests/evaluation/pairs.json").read_text())

    def pair(self, ex, judge, second=None):
        pair = {"executor": ex, "judge": judge}
        if second:
            pair["second_judge"] = second
        return pair

    def test_every_pair_of_pairs_json_is_valid(self):
        for name, provider in self.cfg["providers"].items():
            for pair in provider["pairs"]:
                self.assertEqual(EVAL.check_pair(self.cfg, name, pair), [], name)

    def test_refuses_a_judge_below_the_executor(self):
        pair = self.pair(
            {"model": "anthropic/claude-opus-5-5", "effort": "medium"},
            {"model": "anthropic/claude-sonnet-5-5", "effort": "max"},
        )
        self.assertEqual(len(EVAL.check_pair(self.cfg, "anthropic", pair)), 1)

    def test_same_model_needs_more_effort(self):
        same = {"model": "xai/grok-4.7", "effort": "high"}
        self.assertEqual(
            len(EVAL.check_pair(self.cfg, "xai", self.pair(same, same))), 1
        )
        more = {"model": "xai/grok-4.7", "effort": "max"}
        self.assertEqual(EVAL.check_pair(self.cfg, "xai", self.pair(same, more)), [])

    def test_refuses_a_second_judge_of_the_same_provider(self):
        pair = self.pair(
            {"model": "anthropic/claude-sonnet-5-5", "effort": "medium"},
            {"model": "anthropic/claude-opus-5-5", "effort": "high"},
            {"model": "anthropic/claude-fable-5-1", "effort": "high"},
        )
        self.assertEqual(len(EVAL.check_pair(self.cfg, "anthropic", pair)), 1)

    def test_plan_calls_nothing_and_exits_0(self):
        result = run("run-evaluation.py", "--plan", "--prompts", "C1", "--samples", "1")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Estimate for 6 pairs", result.stdout)


class RunEvaluationScores(unittest.TestCase):
    def setUp(self):
        text = (BIN.parent / "tests/evaluation/evaluation-tests.md").read_text()
        self.prompts = {p["id"]: p for p in EVAL.parse_prompts(text)}

    def judgment(self, value, r6=None):
        scores = {c: {"score": value, "evidence": ""} for c in EVAL.CRITERIA}
        scores["R6"]["score"] = r6
        return {"scores": scores, "main_defect": ""}

    def test_reads_13_prompts_and_the_r6_prompts_of_the_rubric(self):
        self.assertEqual(len(self.prompts), 13)
        r6 = sorted(i for i, p in self.prompts.items() if p["r6"])
        self.assertEqual(r6, ["C1", "K1", "T1", "T2", "T3", "X1"])

    def test_pass_needs_80_percent_and_every_gate(self):
        _, total, available, gates, passed = EVAL.score(
            self.judgment(2), self.prompts["C2"]
        )
        self.assertEqual((total, available, gates, passed), (16, 16, True, True))
        low = self.judgment(2)
        low["scores"]["R2"]["score"] = 0
        self.assertFalse(EVAL.score(low, self.prompts["C2"])[3])

    def test_check_judgment_takes_only_0_1_2_or_null(self):
        EVAL.check_judgment(self.judgment(2))
        EVAL.check_judgment(self.judgment(None))
        for value in (3, -1, True, "2"):
            with self.assertRaises(ValueError):
                EVAL.check_judgment(self.judgment(value))
        with self.assertRaises(ValueError):
            EVAL.check_judgment({"scores": {}, "main_defect": ""})

    def test_r6_counts_only_where_it_applies(self):
        _, total, available, _, _ = EVAL.score(
            self.judgment(2, r6=2), self.prompts["K1"]
        )
        self.assertEqual((total, available), (18, 18))
        _, total, available, _, _ = EVAL.score(
            self.judgment(2, r6=2), self.prompts["K2"]
        )
        self.assertEqual((total, available), (16, 16))

    def test_human_test_takes_gaps_failed_gates_and_a_sample(self):
        def row(file, total, gates="yes"):
            return {
                "response_file": file,
                "total": total,
                "gates_passed": gates,
                "date": "d",
                "model": "m",
                "provider": "p",
                "rules_version": "v",
                "prompt_id": "C1",
                "domain": "Clear",
            }

        rows = [row("a", 16), row("a", 10), row("b", 16, "no"), row("b", 16)]
        rows += [row(f"c{n}", 16) for n in range(5)]
        chosen = {
            r["response_file"]: r["reason"] for r in EVAL.human_test_rows(rows, "seed")
        }
        self.assertEqual(chosen["a"], "judges differ by more than 3 points")
        self.assertEqual(chosen["b"], "a judge failed a gate")
        self.assertEqual(sum(v == "random sample" for v in chosen.values()), 2)


class RunEvaluationUnit(unittest.TestCase):
    """One unit of work with a stub in place of the API: no network."""

    def test_refuses_an_answer_cut_by_max_output_tokens(self):
        cfg = json.loads((BIN.parent / "tests/evaluation/pairs.json").read_text())
        body = {
            "status": "incomplete",
            "incomplete_details": {"reason": "max_output_tokens"},
            "usage": {"output_tokens": 7996},
            "output": [],
        }

        def urlopen(request, timeout):
            return contextlib.nullcontext(io.BytesIO(json.dumps(body).encode()))

        original = EVAL.urllib.request.urlopen
        EVAL.urllib.request.urlopen = urlopen
        self.addCleanup(setattr, EVAL.urllib.request, "urlopen", original)
        model = {"model": "google/gemini-3.8-flash", "effort": "medium"}
        with self.assertRaisesRegex(RuntimeError, "max_output_tokens"):
            EVAL.call(cfg, "key", model, "executor", "", "text")

    def test_writes_the_response_the_judgments_and_one_row_per_judge(self):
        cfg = json.loads((BIN.parent / "tests/evaluation/pairs.json").read_text())
        pair = cfg["providers"]["anthropic"]["pairs"][0]
        prompt = EVAL.parse_prompts(
            (BIN.parent / "tests/evaluation/evaluation-tests.md").read_text()
        )[1]
        judgment = {
            "scores": {c: {"score": 2, "evidence": "ok"} for c in EVAL.CRITERIA},
            "main_defect": "none",
        }
        usage = {"input_tokens": 10, "output_tokens": 5, "cost": {"total_cost": 0.01}}

        def stub(cfg, key, model, role, instructions, text, schema=None):
            return (json.dumps(judgment) if schema else "# Headline\n"), usage, 0.1

        original, EVAL.call = EVAL.call, stub
        self.addCleanup(setattr, EVAL, "call", original)
        with tempfile.TemporaryDirectory() as folder:
            ctx = {
                "date": "2026-10-26",
                "version": "3.2.0",
                "rules": "",
                "schema": EVAL.judge_schema(),
                "judge_instructions": "",
            }
            calls, rows, errors = EVAL.run_unit(
                cfg, "key", Path(folder), ctx, "anthropic", pair, prompt, 1
            )
            response = Path(folder) / rows[0]["response_file"]
            self.assertTrue(
                response.read_text().startswith("anthropic/claude-sonnet-5-5")
            )
            self.assertEqual(len(list(Path(folder).rglob("*.json"))), 2)
        self.assertEqual(errors, [])
        self.assertEqual(len(calls), 3)
        self.assertEqual(
            [r["grader"] for r in rows],
            ["anthropic/claude-opus-5-5@high", "openai/gpt-6-astra@high"],
        )
        self.assertTrue(all(r["pass"] == "yes" for r in rows))
        self.assertEqual(set(rows[0]), set(EVAL.HEADER))


class RunEvaluationMerge(unittest.TestCase):
    """The JSONL of each provider, merged into the final view of a run."""

    def unit(self, folder, name, fail_second_judge=False):
        cfg = json.loads((BIN.parent / "tests/evaluation/pairs.json").read_text())
        pair = cfg["providers"][name]["pairs"][0]
        prompt = EVAL.parse_prompts(
            (BIN.parent / "tests/evaluation/evaluation-tests.md").read_text()
        )[0]
        judgment = {
            "scores": {c: {"score": 2, "evidence": "ok"} for c in EVAL.CRITERIA},
            "main_defect": "none",
        }
        usage = {"input_tokens": 10, "output_tokens": 5, "cost": {"total_cost": 0.5}}

        def stub(cfg, key, model, role, instructions, text, schema=None):
            if fail_second_judge and model == pair["second_judge"]:
                raise EVAL.CallError("incomplete answer", usage)
            return (json.dumps(judgment) if schema else "# Headline\n"), usage, 0.1

        original, EVAL.call = EVAL.call, stub
        self.addCleanup(setattr, EVAL, "call", original)
        ctx = {
            "date": "2026-10-28",
            "version": "3.2.0",
            "rules": "",
            "schema": EVAL.judge_schema(),
            "judge_instructions": "",
        }
        results = folder / "results"
        results.mkdir(exist_ok=True)
        with (results / f"{name}.jsonl").open("a") as out:
            EVAL.write_records(
                out,
                name,
                *EVAL.run_unit(cfg, "key", folder, ctx, name, pair, prompt, 1),
            )

    def test_merges_each_provider_and_reports_the_failed_calls(self):
        with tempfile.TemporaryDirectory() as name:
            folder = Path(name)
            self.unit(folder, "anthropic")
            self.unit(folder, "xai", fail_second_judge=True)
            with (folder / "results" / "xai.jsonl").open("a") as out:
                out.write('{"kind": "sco')
            with contextlib.redirect_stdout(io.StringIO()) as printed:
                code = EVAL.merge(folder)
            scores = (folder / "scores.csv").read_text().splitlines()
            calls = (folder / "calls.csv").read_text().splitlines()
            self.assertTrue((folder / "human-test.csv").exists())
        self.assertEqual(code, 1)
        self.assertEqual(len(scores), 1 + 3)
        self.assertEqual(calls[0].split(","), EVAL.CALL_FIELDS)
        self.assertEqual(len(calls), 1 + 6)
        self.assertEqual(sum(",failed," in c for c in calls), 1)
        text = printed.getvalue()
        self.assertIn("Calls: 6, 1 failed. Cost: 3.00 USD.", text)
        self.assertIn("xai: C1-s1 judge google/gemini-4-argon: incomplete answer", text)
        self.assertIn("xai: line 6 is not a record", text)

    def test_the_ci_matrix_names_each_provider_of_pairs_json(self):
        cfg = json.loads((BIN.parent / "tests/evaluation/pairs.json").read_text())
        ci = (BIN.parent / ".gitlab-ci.yml").read_text()
        matrix = re.search(r"- PROVIDER: \[(.*)\]", ci).group(1)
        self.assertEqual([p.strip() for p in matrix.split(",")], list(cfg["providers"]))


if __name__ == "__main__":
    unittest.main()
