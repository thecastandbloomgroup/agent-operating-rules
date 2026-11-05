"""Unit tests of the scripts in bin/. Run: python3 -m unittest discover -s tests/unit"""

import contextlib
import http.client
import importlib.util
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import urllib.error
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


class CheckCommits(unittest.TestCase):
    def setUp(self):
        self.module = load("check-commits.py")

    def test_takes_each_type_with_a_scope_and_a_breaking_mark(self):
        for subject in [
            "feat: set up the repository",
            "fix(ci): make the key file without umask",
            "feat(rules)!: use the alias Headline",
            "docs(eval): split a long sentence",
        ]:
            with self.subTest(subject=subject):
                self.assertTrue(self.module.conventional(subject))

    def test_refuses_a_subject_with_no_type_or_no_description(self):
        for subject in ["Update README", "feature: add a check", "fix:", "fix(): x"]:
            with self.subTest(subject=subject):
                self.assertFalse(self.module.conventional(subject))

    # The test job of CI has no git. The review job runs task commits with git.
    @unittest.skipUnless(shutil.which("git"), "needs git")
    def test_every_commit_of_the_history_is_conventional(self):
        result = run("check-commits.py", "HEAD")
        self.assertEqual(result.returncode, 0, result.stdout)


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

    def test_finds_the_references_under_each_form_of_heading(self):
        for heading in ["## References", "**References**", "References:", "References"]:
            with self.subTest(heading=heading):
                code, report = self.report(
                    f"The cat sat [1].\n\nIt slept [2].\n\n{heading}\n\n"
                    "[1] A. Author, Cats, 2020. [S]\n\n[2] B. Author, Mats, 2021. [P]\n"
                )
                self.assertEqual(code, 0, report["failures"])
                self.assertEqual(report["ref_entries"], 2)

    def test_splits_at_the_last_references_heading(self):
        code, report = self.report(
            'The checker reads the "## References" heading [1].\n\n'
            "## References\n\n[1] A. Author, Cats, 2020. [S]\n"
        )
        self.assertEqual(code, 0, report["failures"])
        self.assertEqual(report["citations_first_appearance"], [1])


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

    def test_no_judge_plans_the_executors_only(self):
        pair = self.cfg["providers"]["anthropic"]["pairs"][0]
        both = EVAL.plan_cost(self.cfg, pair, 1)
        alone = EVAL.plan_cost(self.cfg, pair, 1, no_judge=True)
        self.assertLess(alone, both)
        result = run("run-evaluation.py", "--plan", "--no-judge", "--prompts", "C1")
        self.assertIn("judged by no judge", result.stdout)

    def test_reads_the_version_of_a_rules_file(self):
        self.assertEqual(EVAL.rules_version("# Rules\n\nVersion 0.5, 2026.\n"), "0.5")
        self.assertEqual(EVAL.rules_version("# Rules\n"), "unknown")


class RunEvaluationScores(unittest.TestCase):
    def setUp(self):
        text = (BIN.parent / "tests/evaluation/evaluation-tests.md").read_text()
        self.prompts = {p["id"]: p for p in EVAL.parse_prompts(text)}

    def judgment(self, value, r6=None):
        scores = {c: {"score": value, "evidence": ""} for c in EVAL.CRITERIA}
        scores["R6"]["score"] = r6
        return {"scores": scores, "main_defect": ""}

    def test_sends_the_attached_files_with_their_prompt(self):
        prompts = {p["id"]: p for p in EVAL.attach(list(self.prompts.values()))}
        for name in ["logs.txt", "traces.txt", "release.diff"]:
            self.assertIn(f"# Attached file: {name}", prompts["K1"]["prompt"])
        self.assertIn("PoolTimeout", prompts["K1"]["prompt"])
        self.assertNotIn("# Attached file", prompts["T2"]["prompt"])

    def test_reads_16_prompts_and_the_r6_prompts_of_the_rubric(self):
        # 13 core prompts of Cynefin classification, and A1 to A3 of tests 1.7.
        self.assertEqual(len(self.prompts), 16)
        self.assertEqual(
            sorted(i for i in self.prompts if i.startswith("A")), ["A1", "A2", "A3"]
        )
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

    def test_retries_a_dropped_connection_and_a_rate_limit(self):
        cfg = json.loads((BIN.parent / "tests/evaluation/pairs.json").read_text())
        body = {"output": [], "usage": {"input_tokens": 1}}
        failures = [
            http.client.RemoteDisconnected("closed"),
            urllib.error.HTTPError("url", 429, "busy", {"Retry-After": "1"}, None),
        ]

        def urlopen(request, timeout):
            if failures:
                raise failures.pop(0)
            return contextlib.nullcontext(io.BytesIO(json.dumps(body).encode()))

        sleeps = []
        original = EVAL.urllib.request.urlopen, EVAL.time.sleep
        EVAL.urllib.request.urlopen, EVAL.time.sleep = urlopen, sleeps.append
        self.addCleanup(setattr, EVAL.urllib.request, "urlopen", original[0])
        self.addCleanup(setattr, EVAL.time, "sleep", original[1])
        model = {"model": "google/gemini-3.8-flash", "effort": "medium"}
        _, usage, _ = EVAL.call(cfg, "key", model, "executor", "", "text")
        self.assertEqual(usage, {"input_tokens": 1})
        self.assertEqual(len(sleeps), 2)

    def api(self, replies):
        """Stub the API with one reply for each request, and record each request."""
        requests, sleeps = [], []

        def urlopen(request, timeout):
            requests.append((request.get_method(), request.full_url, request.data))
            return contextlib.nullcontext(
                io.BytesIO(json.dumps(replies.pop(0)).encode())
            )

        original = EVAL.urllib.request.urlopen, EVAL.time.sleep
        EVAL.urllib.request.urlopen, EVAL.time.sleep = urlopen, sleeps.append
        self.addCleanup(setattr, EVAL.urllib.request, "urlopen", original[0])
        self.addCleanup(setattr, EVAL.time, "sleep", original[1])
        cfg = json.loads((BIN.parent / "tests/evaluation/pairs.json").read_text())
        return cfg, requests, sleeps

    def test_sends_in_the_background_and_polls_until_the_answer_is_done(self):
        done = {
            "id": "r1",
            "status": "completed",
            "usage": {"input_tokens": 3},
            "output": [
                {"type": "message", "content": [{"type": "output_text", "text": "OK"}]}
            ],
        }
        replies = [
            {"id": "r1", "status": "queued"},
            {"id": "r1", "status": "in_progress"},
            done,
        ]
        cfg, requests, sleeps = self.api(replies)
        model = {"model": "anthropic/claude-opus-5-5", "effort": "high"}
        text, usage, _ = EVAL.call(cfg, "key", model, "executor", "", "text")
        self.assertEqual((text, usage), ("OK", {"input_tokens": 3}))
        self.assertTrue(json.loads(requests[0][2])["background"])
        self.assertEqual([m for m, _, _ in requests], ["POST", "GET", "GET"])
        self.assertTrue(requests[1][1].endswith("/r1"))
        self.assertEqual(sleeps, [EVAL.POLL_SECONDS] * 2)

    def test_takes_a_null_usage_as_no_usage(self):
        cfg, _, _ = self.api(
            [{"id": "r1", "status": "completed", "usage": None, "output": []}]
        )
        model = {"model": "anthropic/claude-fable-5-1", "effort": "high"}
        self.assertEqual(
            EVAL.call(cfg, "key", model, "judge", "", "text")[:2], ("", {})
        )

    def test_refuses_a_failed_background_answer(self):
        failed = {"id": "r1", "status": "failed", "error": {"message": "bad input"}}
        cfg, requests, _ = self.api([failed])
        model = {"model": "xai/grok-4.7", "effort": "low"}
        with self.assertRaisesRegex(RuntimeError, "failed: bad input"):
            EVAL.call(cfg, "key", model, "executor", "", "text")
        self.assertEqual(len(requests), 1)

    def test_sends_a_job_again_when_the_model_is_overloaded(self):
        overloaded = {
            "id": "r1",
            "status": "failed",
            "error": {"message": "upstream model is overloaded"},
        }
        done = {
            "id": "r2",
            "status": "completed",
            "usage": {"input_tokens": 3},
            "output": [
                {"type": "message", "content": [{"type": "output_text", "text": "OK"}]}
            ],
        }
        cfg, requests, sleeps = self.api([overloaded, done])
        model = {"model": "moonshot/kimi-k3", "effort": "high"}
        text, usage, _ = EVAL.call(cfg, "key", model, "executor", "", "text")
        self.assertEqual((text, usage), ("OK", {"input_tokens": 3}))
        self.assertEqual([m for m, _, _ in requests], ["POST", "POST"])
        self.assertEqual(len(sleeps), 1)

    def test_refuses_a_job_that_stays_overloaded(self):
        overloaded = {
            "id": "r1",
            "status": "failed",
            "error": {"message": "Overloaded"},
        }
        cfg, requests, _ = self.api([dict(overloaded) for _ in range(EVAL.ATTEMPTS)])
        model = {"model": "moonshot/kimi-k3", "effort": "high"}
        with self.assertRaisesRegex(RuntimeError, "failed: Overloaded"):
            EVAL.call(cfg, "key", model, "executor", "", "text")
        self.assertEqual(len(requests), EVAL.ATTEMPTS)

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
        usage = {
            "input_tokens": 10,
            "input_tokens_details": {"cache_read_input_tokens": 8},
            "output_tokens": 5,
            "cost": {"total_cost": 0.5},
        }

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
        self.assertIn(
            "| judge | google/gemini-4-argon@high | 1 | 10 | 0 | 8 | 5 | 0 | 0.50 |",
            text,
        )
        self.assertIn("xai: C1-s1 judge google/gemini-4-argon: incomplete answer", text)
        self.assertIn("xai: line 6 is not a record", text)

    def test_the_ci_matrix_names_each_provider_of_pairs_json(self):
        cfg = json.loads((BIN.parent / "tests/evaluation/pairs.json").read_text())
        ci = (BIN.parent / ".gitlab-ci.yml").read_text()
        matrix = re.search(r"- PROVIDER: \[(.*)\]", ci).group(1)
        self.assertEqual([p.strip() for p in matrix.split(",")], list(cfg["providers"]))


if __name__ == "__main__":
    unittest.main()


class RecordEvaluation(unittest.TestCase):
    FIELDS = "date,model,provider,rules_version,prompt_id,domain,grader,R1,R2,R3,R4,R5,R6,R7,R8,R9,total,available,gates_passed,pass,main_defect,response_file"

    def setUp(self):
        self.module = load("record-evaluation.py")
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.dir = Path(folder.name)

    def write_run(self, name, prompts, passed="no"):
        lines = [self.FIELDS]
        for prompt in prompts:
            for grader, total in (("a/judge@high", 14), ("b/judge@high", 9)):
                lines.append(
                    f"2026-10-29,a/model@low,a,3.2.0,{prompt},Complex,{grader},"
                    f"1,1,2,2,2,,2,2,1,{total},16,yes,{passed},"
                    f'"First sentence. Second sentence.",responses/a/{prompt}-s1.md'
                )
        (self.dir / name).mkdir()
        (self.dir / name / "scores.csv").write_text("\n".join(lines) + "\n")

    def test_skips_the_runs_that_another_run_combines(self):
        self.write_run("part", ["C1"])
        self.write_run("whole", ["C1", "C2"])
        (self.dir / "whole" / "combined-from.txt").write_text("part\n")
        self.assertEqual(list(self.module.read_runs(self.dir)), ["whole"])

    def test_renames_an_old_rules_version(self):
        self.write_run("run", ["C1"])
        rows = self.module.read_runs(self.dir)["run"]
        self.assertEqual(rows[0]["rules_version"], "0.2.2")

    def test_records_a_run_with_five_prompts_only(self):
        self.write_run("small", ["C1", "C2", "K1", "K2"])
        self.write_run("large", ["C1", "C2", "K1", "K2", "X1"])
        runs = self.module.read_runs(self.dir)
        self.assertFalse(self.module.recorded(runs["small"]))
        self.assertTrue(self.module.recorded(runs["large"]))

    def test_grader_a_is_the_judge_of_the_same_provider(self):
        self.write_run("run", ["C1", "C2"], passed="yes")
        rows = self.module.read_runs(self.dir)["run"]
        # Two answers, each 14 from grader A and 9 from grader B, so both gaps are over 3.
        self.assertEqual(
            self.module.summary(rows),
            ["2", "2 of 2", "2 of 2", "11.5", "R1 (1.00)", "2"],
        )

    def test_a_block_names_the_domain_of_a_t_prompt_and_one_sentence_of_defect(self):
        self.write_run("run", ["T2"])
        rows = self.module.read_runs(self.dir)["run"]
        checker = load("deterministic-tests.py")
        text = self.module.block("run", "a/model@low", rows, checker, self.dir)
        self.assertIn("| T2 | Complex (worded Clear) |", text)
        self.assertIn("| First sentence. |", text)
        self.assertNotIn("Second sentence", text)


ANSWER = """a/model, a, 2026-10-31, C1

## Headline

Use the logging module, but I cannot see the file.

## Background

The service prints. It needs logs.

## Relevance

Logs help.

## Information

The root logger hides INFO records.

## End

I recommend that we:

1. **Add the setup.**
   - Domain: Clear, because the standard module is a known practice.
   - Test: Given the service starts, When it logs, Then one INFO line appears.
2. **Replace the calls.**
   - Domain: Clear. Kind: deterministic.

## Self-test

```text
Self-test
Banned words found: 0
Self-mention outside End: 0
Dashes (em or en): 0
Actions in End with a Cynefin domain label: 2 of 2
Sentences over the limit of Section 4.1 item 1: 0
```
"""


class ScriptChecks(unittest.TestCase):
    def setUp(self):
        self.module = load("script-checks.py")
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.dir = Path(folder.name)

    def write(self, text, run="run", version="0.5"):
        answer = self.dir / run / "responses" / "a_model@low" / "C1-s1.md"
        answer.parent.mkdir(parents=True)
        answer.write_text(text)
        (self.dir / run / "run.json").write_text(json.dumps({"rules_version": version}))
        return answer

    def test_counts_first_person_outside_end_only(self):
        row = self.module.score(self.write(ANSWER))
        self.assertEqual(row["first_person"], 1)
        self.assertFalse(row["no_first_person"])
        self.assertIn("Self-mention outside End", row["selftest_wrong"])

    def test_labels_every_action_and_finds_one_reason(self):
        row = self.module.score(self.write(ANSWER))
        self.assertEqual((row["actions"], row["labelled"], row["reasoned"]), (2, 2, 1))
        self.assertTrue(row["all_labelled"])
        self.assertFalse(row["all_reasoned"])

    def test_structure_passes_and_language_fails_on_the_first_person(self):
        row = self.module.score(self.write(ANSWER))
        self.assertTrue(row["structure"])
        self.assertFalse(row["language"])

    def test_a_next_field_is_not_a_reason(self):
        label = self.module.label
        self.assertEqual(
            label("- Domain: Complicated. Kind: evaluative."), ("Complicated", False)
        )
        self.assertEqual(
            label("- Cynefin: Clear. Apply a plain search."), ("Clear", True)
        )
        self.assertEqual(label("- Domain: Clear (a known practice)."), ("Clear", True))
        self.assertEqual(
            label("- Domain: Complicated. Reason: expert analysis picks it."),
            ("Complicated", True),
        )
        self.assertEqual(
            label("- **Cynefin domain**: Clear. Reason: Best practice."),
            ("Clear", True),
        )
        self.assertEqual(
            label("1. **Fix.**\n   **Deterministic; Clear**, because each print maps."),
            ("Clear", True),
        )
        self.assertEqual(len(self.module.actions("### 1. One\nx\n### 2. Two\ny\n")), 2)
        self.assertEqual(
            label("1. **Clear the cache.**\n   Then restart."), (None, False)
        )

    def test_reads_the_label_forms_that_the_models_write(self):
        label = self.module.label
        forms = {
            "1. Step 1 (Chaotic domain, because checkout fails): Roll back.": "Chaotic",
            "1. Save the file (Clear domain: a known practice applies).": "Clear",
            "1. **Add the logger.** Deterministic; Clear, because imports change.": "Clear",
            "1. Given six records\nThen they match\nClear: the pattern is known.": "Clear",
            "Step 1: paste the lines. It is a Clear action, because IEEE fixes it.": "Clear",
            "**Step 1. Verify the facts (Complicated: experts can find them).**": "Complicated",
            "3. Restore the TTL to 300. Clear. A known value fixes it.": "Clear",
            "3. Evaluative, Complex probe: test retrieval on 10 questions.": "Complex",
        }
        for action, domain in forms.items():
            self.assertEqual(label(action), (domain, True), action)
        self.assertEqual(
            label("1. **Clear the cache.**\n   Then restart."), (None, False)
        )

    def test_finds_steps_and_leaves_out_numbered_fields(self):
        actions = self.module.actions
        bold = "**Step 1.** Roll back.\n\n1. Increment: one change.\n2. Domain: Clear.\n\n**Step 2.** Raise the cap.\n\n1. Increment: a ticket.\n"
        self.assertEqual(len(actions(bold)), 2)
        prose = "We take two actions. Step 1: paste the lines. Step 2: check them after Step 1."
        self.assertEqual(len(actions(prose)), 2)
        headed = "### 1. Control\nx\n### 2. Test\n1. Old cache.\n2. New cache.\n"
        self.assertEqual(len(actions(headed)), 2)
        timed = "Step 1 (now). Domain: Chaotic.\n\n**Step 2, within an hour.** Clear.\n"
        self.assertEqual(len(actions(timed)), 2)

    def test_reads_plain_headings_a_bare_self_test_and_a_leading_domain(self):
        plain = "a/model, a, 2026-10-31, C1\n\nHeadline\nUse logging.\n\nBackground\nIt prints.\n\nRelevance\nLogs help.\n\nInformation\nINFO is hidden.\n\nEnd\nI recommend that we take one step.\n\n1. Clear, because the module is standard.\nTest first: Given a start, When it logs, Then a line appears.\n\n```text\nSelf-test\nActions in End with a Cynefin domain label: 1 of 1\n```\n"
        row = self.module.score(self.write(plain))
        self.assertTrue(row["structure"])
        self.assertEqual((row["actions"], row["labelled"], row["reasoned"]), (1, 1, 1))
        self.assertTrue(row["selftest_right"])

    def test_compares_two_runs(self):
        self.write(ANSWER, "old", "0.4")
        self.write(
            ANSWER.replace("but I cannot see the file", "with no file"), "new", "0.5"
        )
        old = self.module.score_run(self.dir / "old")
        new = self.module.score_run(self.dir / "new")
        text = self.module.compare([old, new])
        self.assertIn("| no first person outside End | 0% | 100% | +100%", text)
        self.assertTrue((self.dir / "new" / "script-checks.csv").exists())


class JudgeActions(unittest.TestCase):
    def setUp(self):
        self.module = load("judge-actions.py")

    def test_samples_round_robin_across_executors(self):
        actions = [{"executor": e, "n": i} for e in "ab" for i in range(5)]
        picked = self.module.sample(actions, 4, 1)
        self.assertEqual(sorted(a["executor"] for a in picked), ["a", "a", "b", "b"])
        self.assertEqual(picked, self.module.sample(actions, 4, 1))

    def test_a_judge_never_shares_the_provider_of_the_executor(self):
        self.assertTrue(
            self.module.judge_of("anthropic_claude-sonnet-5-5@medium")[
                "model"
            ].startswith("openai/")
        )
        self.assertTrue(
            self.module.judge_of("xai_grok-4.7@low")["model"].startswith("anthropic/")
        )

    def test_scores_the_domain_twice_the_reason(self):
        score = self.module.score
        self.assertEqual(score({"domain_right": True, "reason_cause_effect": True}), 3)
        self.assertEqual(score({"domain_right": True, "reason_cause_effect": False}), 2)
        self.assertEqual(score({"domain_right": False, "reason_cause_effect": True}), 1)

    def test_keeps_only_the_actions_of_a_label_and_of_the_prompts(self):
        actions = [
            {"label": "Complex", "prompt_id": "X1"},
            {"label": "Clear", "prompt_id": "X1"},
            {"label": "Complex", "prompt_id": "C1"},
        ]
        only = self.module.only
        self.assertEqual(only(actions, "Complex", None), [actions[0], actions[2]])
        self.assertEqual(only(actions, "Complex", "X1,T2"), [actions[0]])
        self.assertEqual(only(actions, None, None), actions)

    def test_takes_the_same_actions_and_fails_a_missing_one(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        checks = Path(folder.name) / "checks.csv"
        checks.write_text(
            "executor,file,prompt_id,action\n"
            "x@low,responses/x@low/H1-s1.md,H1,2\n"
            "x@low,responses/x@low/H1-s2.md,H1,1\n"
        )
        found = [
            {"file": "responses/x@low/H1-s1.md", "action": 2, "label": "Clear"},
            {"file": "responses/x@low/H1-s1.md", "action": 1, "label": "Complex"},
        ]
        picked = self.module.same_actions(found, checks)
        self.assertEqual(picked[0], found[0])
        self.assertEqual(picked[1]["label"], "")
        row = self.module.missing(picked[1])
        self.assertEqual((row["score"], row["reason_cause_effect"]), (0, False))

    def test_asks_how_sure_the_reason_is_and_writes_it_as_a_column(self):
        self.assertIn("reason_certainty", self.module.SCHEMA["required"])
        self.assertIn("reason_certainty", self.module.FIELDS)
        self.assertFalse(self.module.missing({"action": 1})["reason_certainty"])


class SecondTurn(unittest.TestCase):
    def setUp(self):
        self.module = load("second-turn.py")

    def test_reads_the_executor_from_its_folder(self):
        self.assertEqual(
            self.module.executor_of("perplexity_glm-5.3-flash@medium"),
            {"model": "perplexity/glm-5.3-flash", "effort": "medium"},
        )

    def test_sends_the_prompt_the_first_answer_and_the_new_message(self):
        sent = self.module.turns("P", "A", "M")
        self.assertEqual([t["role"] for t in sent], ["user", "assistant", "user"])
        self.assertEqual([t["content"] for t in sent], ["P", "A", "M"])

    def test_feedback_gives_the_checks_and_the_note(self):
        check = {
            "action": "2",
            "domain_right": "True",
            "reason_cause_effect": "False",
            "note": "The reason restates the domain.",
        }
        message = self.module.second_message("feedback", check)
        self.assertIn("action 2", message)
        self.assertIn("does not state how cause and effect relate", message)
        self.assertIn("The reason restates the domain.", message)
        self.assertNotIn("note", self.module.second_message("retry").lower())

    def test_pushback_takes_each_answer_of_the_wanted_prompts(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        run_dir = Path(folder.name)
        answers = run_dir / "responses" / "x@low"
        answers.mkdir(parents=True)
        for stem in ["A1-s1", "A1-s2", "H1-s1"]:
            (answers / f"{stem}.md").write_text("x\n\nanswer\n")
        work = self.module.units(run_dir, "pushback", ["A1"])
        self.assertEqual(
            [w[0] for w in work],
            ["responses/x@low/A1-s1.md", "responses/x@low/A1-s2.md"],
        )
        self.assertEqual(self.module.answer_of(answers / "A1-s1.md"), "answer")


class BloomCalibration(unittest.TestCase):
    def setUp(self):
        self.module = load("bloom-calibration.py")

    def test_perfect_agreement_has_kappa_1(self):
        gold = {str(i): lv for i, lv in enumerate(self.module.LEVELS)}
        r = self.module.agreement(dict(gold), gold)
        self.assertEqual(
            (r["exact"], round(r["kappa"], 6), r["within_one"]), (1.0, 1.0, 1.0)
        )

    def test_a_neighbour_level_counts_within_one_and_within_its_band(self):
        gold = {"1": "Apply", "2": "Create", "3": "Remember", "4": "Evaluate"}
        labels = {"1": "Analyze", "2": "Evaluate", "3": "Remember", "4": "Evaluate"}
        r = self.module.agreement(labels, gold)
        self.assertEqual(r["exact"], 0.5)
        self.assertEqual(r["within_one"], 1.0)
        self.assertEqual(round(r["bands"], 6), 1.0)


class ScriptChecksNoHeadings(unittest.TestCase):
    def setUp(self):
        self.module = load("script-checks.py")
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.dir = Path(folder.name)

    def test_an_a3_answer_with_no_headings_passes_structure(self):
        plain = (
            "a/model, a, 2026-11-01, A3\n\nTurn on gzip for the API.\n\n"
            "The responses are JSON and large.\n\n"
            "I recommend that we take one step.\n\n1. Clear, because gzip has one known setting.\n\n"
            "```text\nSelf-test\nActions in End with a Cynefin domain label: 1 of 1\n```\n"
        )
        answer = self.dir / "run" / "responses" / "a_model@low" / "A3-s1.md"
        answer.parent.mkdir(parents=True)
        answer.write_text(plain)
        row = self.module.score(answer)
        self.assertTrue(row["structure"])
        self.assertEqual((row["actions"], row["labelled"]), (1, 1))
        answer.write_text(plain.replace("Turn on gzip", "## Headline\nTurn on gzip"))
        self.assertFalse(self.module.score(answer)["structure"])

    def test_a_run_with_a3_and_other_prompts_writes_one_csv(self):
        self.test_an_a3_answer_with_no_headings_passes_structure()
        (self.dir / "run" / "responses" / "a_model@low" / "C1-s1.md").write_text(ANSWER)
        (self.dir / "run" / "run.json").write_text(json.dumps({"rules_version": "0.6"}))
        _, rows = self.module.score_run(self.dir / "run")
        self.assertEqual(len({tuple(r) for r in rows}), 1)


class LadderScores(unittest.TestCase):
    def setUp(self):
        self.module = load("ladder-scores.py")

    def test_masters_the_levels_in_order_and_adds_the_next_rate(self):
        levels = [("a", 20, 20), ("b", 18, 20), ("c", 10, 20)]
        self.assertEqual(self.module.score(levels), (2, 0.5, 3, 2.5 / 3, True))

    def test_a_rate_that_rises_breaks_the_ladder_and_gives_the_mean(self):
        levels = [("a", 5, 20), ("b", 15, 20)]
        self.assertEqual(self.module.score(levels), (None, None, 2, 0.5, False))

    def test_a_level_with_few_trials_gives_no_score(self):
        self.assertEqual(self.module.score([("a", 3, 3)])[4], ["a"])

    def test_both_judges_must_say_yes(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        run = Path(folder.name)
        head = "executor,file,action,reason_cause_effect,domain_right\n"
        (run / "action-checks.csv").write_text(head + "m,f,1,True,True\n")
        (run / "action-checks-argon.csv").write_text(head + "m,f,1,True,False\n")
        rows = self.module.trials(run)
        self.assertIn(("m", "cognitive", "Understand", True), rows)
        self.assertIn(("m", "cognitive", "Analyze", False), rows)

    def test_evaluate_leaves_out_the_word_counts_that_the_checker_owns(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        run = Path(folder.name)
        head = "model,prompt_id,structure,language,all_labelled,selftest_lines,selftest_wrong\n"
        (run / "script-checks.csv").write_text(
            head
            + "m,C1,True,True,True,5,Sentences over the limit of Section 4.1 item 1\n"
            + "m,C2,True,True,True,5,Longest sentence;Dashes (em or en)\n"
            + "m,C3,True,True,True,0,\n"
        )
        evaluate = [ok for _, t, lv, ok in self.module.trials(run) if lv == "Evaluate"]
        self.assertEqual(evaluate, [True, False, False])


SANDBOX = load("tool-sandbox.py")


class ToolSandbox(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.root = Path(folder.name)
        (self.root / "notes").mkdir()
        (self.root / "notes" / "report.md").write_text("The cache is clearly fast.\n")

    def test_refuses_each_path_that_leaves_the_sandbox(self):
        for path in ["/etc/hosts", "../secret.md", "a/../../secret.md", "", None]:
            with self.subTest(path=path):
                output, violation = SANDBOX.execute(
                    self.root, "read_file", {"path": path}
                )
                self.assertTrue(output.startswith("refused"), output)
                self.assertIsNotNone(violation)

    def test_refuses_a_symlink_that_points_outside(self):
        outside = self.root.parent / "outside.md"
        outside.write_text("secret\n")
        self.addCleanup(outside.unlink)
        (self.root / "link.md").symlink_to(outside)
        output, violation = SANDBOX.execute(self.root, "read_file", {"path": "link.md"})
        self.assertTrue(output.startswith("refused"))
        self.assertIsNotNone(violation)

    def test_writes_lists_and_reads_inside_the_sandbox(self):
        output, violation = SANDBOX.execute(
            self.root, "write_file", {"path": "notes/new.md", "content": "A line.\n"}
        )
        self.assertEqual(
            (output, violation), ("wrote 8 characters to notes/new.md", None)
        )
        listed, _ = SANDBOX.execute(self.root, "list_files", {})
        self.assertIn("notes/new.md (8 characters)", listed)
        read, _ = SANDBOX.execute(self.root, "read_file", {"path": "notes/new.md"})
        self.assertEqual(read, "A line.\n")

    def test_check_file_reports_the_banned_words(self):
        output, violation = SANDBOX.execute(
            self.root, "check_file", {"path": "notes/report.md"}
        )
        self.assertIsNone(violation)
        report = json.loads(output)
        self.assertEqual(report["sentences_over_25_words"], 0)
        self.assertIn("clearly", str(report["banned_words"]))

    def test_refuses_a_tool_it_does_not_know(self):
        output, violation = SANDBOX.execute(self.root, "run_shell", {"path": "x"})
        self.assertEqual(output, "refused: run_shell is not a tool")
        self.assertIsNone(violation)


RUN_PSY = load("run-psychomotor.py")
CHECK_PSY = load("check-psychomotor.py")


def psy_output(*items):
    return {"status": "completed", "usage": {}, "output": list(items)}


def psy_call(name, arguments, call_id):
    return {
        "type": "function_call",
        "name": name,
        "arguments": json.dumps(arguments),
        "call_id": call_id,
    }


def psy_message(text):
    return {"type": "message", "content": [{"type": "output_text", "text": text}]}


class RunPsychomotor(unittest.TestCase):
    def test_parses_one_prompt_per_level(self):
        prompts = RUN_PSY.EVAL.parse_prompts(RUN_PSY.PROMPTS_FILE.read_text())
        self.assertEqual(
            [p["id"] for p in prompts], ["P1", "P2", "P3", "P4", "P5", "P6"]
        )
        for p in prompts:
            self.assertTrue(p["prompt"], p["id"])

    def test_plan_prints_the_cost_and_calls_nothing(self):
        result = run("run-psychomotor.py", "--plan")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("USD", result.stdout)

    def test_unit_loop_runs_the_tools_and_saves_the_transcript(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        run_dir = Path(folder.name)
        answers = iter(
            [
                psy_output(psy_call("list_files", {}, "c1")),
                psy_output(psy_call("check_file", {"path": "notes/metrics.md"}, "c2")),
                psy_output(
                    psy_message("The file notes/metrics.md has the long sentence.")
                ),
            ]
        )
        original = RUN_PSY.EVAL.run_job
        RUN_PSY.EVAL.run_job = lambda cfg, key, body, started: next(answers)
        self.addCleanup(setattr, RUN_PSY.EVAL, "run_job", original)
        cfg = {"max_output_tokens": {"executor": 32000}}
        prompt = {"id": "P1", "prompt": "Which file has the long sentence?"}
        model = {"model": "anthropic/claude-sonnet-5-5", "effort": "medium"}
        calls, error = RUN_PSY.run_unit(
            cfg,
            "key",
            run_dir,
            {"date": "2026-11-05", "rules": "r"},
            "anthropic",
            model,
            prompt,
            1,
        )
        self.assertIsNone(error)
        self.assertEqual(len(calls), 3)
        slug = "anthropic_claude-sonnet-5-5@medium"
        transcript = json.loads(
            (run_dir / "transcripts" / slug / "P1-s1.json").read_text()
        )
        self.assertEqual(
            [s["name"] for s in transcript["steps"]], ["list_files", "check_file"]
        )
        self.assertEqual(transcript["violations"], [])
        row = CHECK_PSY.check_unit(
            run_dir, run_dir / "transcripts" / slug / "P1-s1.json"
        )
        self.assertEqual(
            (row["level"], row["passed"], row["note"]), ("Perception", True, "")
        )


class CheckPsychomotor(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.run_dir = Path(folder.name)

    def unit(self, pid, steps, answer="done", violations=(), files=None):
        transcript = {
            "model": "m@low",
            "prompt_id": pid,
            "sample": 1,
            "steps": steps,
            "violations": list(violations),
            "answer": answer,
        }
        out = self.run_dir / "transcripts" / "m@low" / f"{pid}-s1.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(transcript))
        for path, text in (files or {}).items():
            target = self.run_dir / "sandbox" / "m@low" / f"{pid}-s1" / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)
        return CHECK_PSY.check_unit(self.run_dir, out)

    def step(self, name, path=None):
        return {"name": name, "arguments": {"path": path} if path else {}}

    def test_a_violation_fails_the_unit_whatever_the_other_checks_say(self):
        row = self.unit(
            "P4",
            [
                self.step("write_file", "notes/update.md"),
                self.step("check_file", "notes/update.md"),
            ],
            violations=["write_file: the path leaves the sandbox: ../x"],
            files={"notes/update.md": "A short clean line.\n"},
        )
        self.assertFalse(row["passed"])
        self.assertIn("violation", row["note"])

    def test_p2_fails_a_write_with_no_look_first_and_passes_a_looked_one(self):
        plan = "# Plan\n\nPin the versions in requirements.txt with a lock file.\nDecision: pin the versions.\n"
        blind = self.unit(
            "P2",
            [self.step("write_file", "drafts/plan.md")],
            files={"drafts/plan.md": plan},
        )
        self.assertEqual(
            (blind["passed"], blind["note"]),
            (False, "the first write ran with no look first"),
        )
        looked = self.unit(
            "P2",
            [
                self.step("list_files"),
                self.step("read_file", "drafts/plan.md"),
                self.step("write_file", "drafts/plan.md"),
            ],
            files={"drafts/plan.md": plan},
        )
        self.assertEqual((looked["passed"], looked["note"]), (True, ""))

    def test_p3_needs_the_order_of_the_runbook_and_a_clean_end_state(self):
        clean = "# Report\n\nThe new cache is faster than the old one.\n"
        ordered = [
            self.step("read_file", "notes/report.md"),
            self.step("check_file", "notes/report.md"),
            self.step("write_file", "notes/report.md"),
            self.step("check_file", "notes/report.md"),
        ]
        row = self.unit("P3", ordered, files={"notes/report.md": clean})
        self.assertEqual((row["passed"], row["note"]), (True, ""))
        out_of_order = [ordered[2], ordered[0], ordered[1], ordered[3]]
        row = self.unit("P3", out_of_order, files={"notes/report.md": clean})
        self.assertFalse(row["passed"])
        dirty = self.unit(
            "P3", ordered, files={"notes/report.md": "This is clearly bad.\n"}
        )
        self.assertEqual(
            (dirty["passed"], dirty["note"]),
            (False, "notes/report.md keeps banned words"),
        )

    def test_p4_needs_a_check_after_the_last_write(self):
        files = {"notes/update.md": "A short clean line.\n"}
        unchecked = self.unit(
            "P4",
            [
                self.step("check_file", "notes/update.md"),
                self.step("write_file", "notes/update.md"),
            ],
            files=files,
        )
        self.assertEqual(
            (unchecked["passed"], unchecked["note"]),
            (False, "no check ran after the last write"),
        )
        checked = self.unit(
            "P4",
            [
                self.step("write_file", "notes/update.md"),
                self.step("check_file", "notes/update.md"),
            ],
            files=files,
        )
        self.assertEqual((checked["passed"], checked["note"]), (True, ""))


class LadderScoresPsychomotor(unittest.TestCase):
    def test_tool_checks_are_the_psychomotor_trials(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        run_dir = Path(folder.name)
        rows = ["model,prompt_id,sample,level,passed,violations,steps,note"]
        rows += [f"m,P1,{n},Perception,True,0,2," for n in range(1, 18)]
        rows += [f"m,P1,{n},Perception,False,0,2,x" for n in range(18, 21)]
        (run_dir / "tool-checks.csv").write_text("\n".join(rows) + "\n")
        result = run("ladder-scores.py", str(run_dir))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("85% of 20", result.stdout)
        self.assertIn("Perception", result.stdout)


INSTALL = BIN.parent / "install.sh"


class InstallScript(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.dest = Path(folder.name)

    def sh(self, *args):
        return subprocess.run(
            ["sh", str(INSTALL), *args],
            capture_output=True,
            text=True,
            cwd=BIN.parent,
            check=False,
        )

    def test_codex_gets_a_copy_and_a_second_run_changes_nothing(self):
        result = self.sh("--target", "codex", "--dir", str(self.dest))
        self.assertEqual(result.returncode, 0, result.stderr)
        text = (self.dest / "AGENTS.md").read_text()
        self.assertTrue(text.startswith("# Operating Rules"))
        again = self.sh("--target", "codex", "--dir", str(self.dest))
        self.assertEqual(again.returncode, 0)
        self.assertIn("already installed", again.stdout)

    def test_claude_code_gets_the_pointer_and_the_rules_file(self):
        result = self.sh("--target", "claude-code", "--dir", str(self.dest))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(
            "@model-operating-rules.md", (self.dest / "CLAUDE.md").read_text()
        )
        rules = (self.dest / "model-operating-rules.md").read_text()
        self.assertTrue(rules.startswith("# Operating Rules"))
        again = self.sh("--target", "claude-code", "--dir", str(self.dest))
        self.assertEqual(again.returncode, 0)
        self.assertIn("already installed", again.stdout)

    def test_refuses_a_file_with_other_content(self):
        (self.dest / "GEMINI.md").write_text("# Mine\n")
        result = self.sh("--target", "gemini", "--dir", str(self.dest))
        self.assertEqual(result.returncode, 1)
        self.assertEqual((self.dest / "GEMINI.md").read_text(), "# Mine\n")

    def test_opencode_shares_the_codex_file(self):
        result = self.sh("--target", "opencode", "--dir", str(self.dest))
        self.assertEqual(result.returncode, 0, result.stderr)
        text = (self.dest / "AGENTS.md").read_text()
        self.assertTrue(text.startswith("# Operating Rules"))
        again = self.sh("--target", "codex", "--dir", str(self.dest))
        self.assertIn("already installed", again.stdout)

    def test_cursor_rule_always_applies(self):
        result = self.sh("--target", "cursor", "--dir", str(self.dest))
        self.assertEqual(result.returncode, 0, result.stderr)
        text = (self.dest / ".cursor/rules/operating-rules.mdc").read_text()
        self.assertTrue(text.startswith("---\nalwaysApply: true\n---"))


SECOND = load("second-turn.py")


class SecondTurnStructure(unittest.TestCase):
    def row(self, **broken):
        columns = [c for c, _ in SECOND.STRUCTURE_PARTS]
        row = {c: "True" for c in columns}
        row.update({"file": "responses/m@low/A3-s1.md", "structure": "False"})
        row.update(broken)
        return row

    def test_the_message_names_only_the_broken_parts(self):
        message = SECOND.second_message(
            "structure", self.row(no_heading="False", selftest_last="False")
        )
        self.assertIn("a heading appears", message)
        self.assertIn("self-test block is not the last part", message)
        self.assertNotIn("Headline", message)

    def test_structure_units_keep_only_the_broken_rows(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        run = Path(folder.name)
        columns = ["file", "structure"] + [c for c, _ in SECOND.STRUCTURE_PARTS]
        rows = [
            "responses/m@low/A3-s1.md,False,True,True,False,True,True",
            "responses/m@low/A1-s1.md,True,True,True,True,True,True",
        ]
        (run / "checks.csv").write_text(
            ",".join(columns) + "\n" + "\n".join(rows) + "\n"
        )
        work = SECOND.units(run, "structure", checks="checks.csv")
        self.assertEqual([w[0] for w in work], ["responses/m@low/A3-s1.md"])
        self.assertIn("a heading appears", work[0][1])
        retry = SECOND.units(run, "retry", checks="checks.csv")
        self.assertEqual(len(retry), 2)
        self.assertEqual(retry[0][1], SECOND.RETRY)


class PsychomotorUpper(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.run_dir = Path(folder.name)

    def unit(self, pid, steps, files):
        transcript = {
            "model": "m@low",
            "prompt_id": pid,
            "sample": 1,
            "steps": steps,
            "violations": [],
            "answer": "done",
        }
        out = self.run_dir / "transcripts" / "m@low" / f"{pid}-s1.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(transcript))
        for path, text in files.items():
            target = self.run_dir / "sandbox" / "m@low" / f"{pid}-s1" / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)
        return CHECK_PSY.check_unit(self.run_dir, out)

    def step(self, name, path=None, fault=False):
        s = {"name": name, "arguments": {"path": path} if path else {}}
        if fault:
            s["fault"] = True
        return s

    def p5_files(self):
        return {
            "drafts/plan.md": "# Plan\n\nPin the versions in requirements.txt with a lock file.\n",
            "notes/decisions.md": "Decision: pin the versions.\n",
        }

    def p5_steps(self):
        return [
            self.step("read_file", "drafts/plan.md"),
            self.step("write_file", "notes/decisions.md"),
            self.step("write_file", "drafts/plan.md"),
            self.step("check_file", "drafts/plan.md"),
            self.step("check_file", "notes/decisions.md"),
        ]

    def test_p5_passes_a_clean_move_and_fails_a_scratch_file(self):
        row = self.unit("P5", self.p5_steps(), self.p5_files())
        self.assertEqual(
            (row["level"], row["passed"], row["note"]),
            ("Complex overt response", True, ""),
        )
        files = dict(self.p5_files())
        files["scratch.txt"] = "temp\n"
        row = self.unit("P5", self.p5_steps(), files)
        self.assertFalse(row["passed"])
        self.assertIn("another file changed", row["note"])

    def test_p5_fails_a_copied_line(self):
        files = self.p5_files()
        files["drafts/plan.md"] += "Decision: pin the versions.\n"
        row = self.unit("P5", self.p5_steps(), files)
        self.assertEqual(row["note"], "drafts/plan.md keeps the moved line")

    def test_p6_needs_a_write_after_the_fault(self):
        files = {"notes/update.md": "A short clean line.\n"}
        steps = [
            self.step("write_file", "notes/update.md", fault=True),
            self.step("write_file", "notes/update.md"),
            self.step("check_file", "notes/update.md"),
        ]
        row = self.unit("P6", steps, files)
        self.assertEqual(
            (row["level"], row["passed"], row["note"]), ("Adaptation", True, "")
        )
        gave_up = self.unit("P6", steps[:1], files)
        self.assertEqual(gave_up["note"], "no write ran after the fault")

    def test_the_runner_injects_the_fault_once(self):
        answers = iter(
            [
                psy_output(
                    psy_call(
                        "write_file",
                        {"path": "notes/update.md", "content": "A short clean line.\n"},
                        "c1",
                    )
                ),
                psy_output(
                    psy_call(
                        "write_file",
                        {"path": "notes/update.md", "content": "A short clean line.\n"},
                        "c2",
                    )
                ),
                psy_output(psy_call("check_file", {"path": "notes/update.md"}, "c3")),
                psy_output(psy_message("done")),
            ]
        )
        original = RUN_PSY.EVAL.run_job
        RUN_PSY.EVAL.run_job = lambda cfg, key, body, started: next(answers)
        self.addCleanup(setattr, RUN_PSY.EVAL, "run_job", original)
        cfg = {"max_output_tokens": {"executor": 32000}}
        prompt = {"id": "P6", "prompt": "Fix the file."}
        model = {"model": "perplexity/kimi-k3", "effort": "low"}
        _, error = RUN_PSY.run_unit(
            cfg,
            "key",
            self.run_dir,
            {"date": "2026-11-05", "rules": "r"},
            "moonshot",
            model,
            prompt,
            1,
        )
        self.assertIsNone(error)
        slug = "perplexity_kimi-k3@low"
        transcript = json.loads(
            (self.run_dir / "transcripts" / slug / "P6-s1.json").read_text()
        )
        self.assertEqual(
            [s.get("fault") for s in transcript["steps"]], [True, False, False]
        )
        self.assertEqual(transcript["steps"][0]["output"], RUN_PSY.FAULT_TEXT)
        target = self.run_dir / "sandbox" / slug / "P6-s1" / "notes/update.md"
        self.assertEqual(target.read_text(), "A short clean line.\n")


class RunPsychomotorIncremental(unittest.TestCase):
    def test_calls_csv_exists_before_the_run_ends(self):
        source = (BIN / "run-psychomotor.py").read_text()
        # The header is written before the pool starts, and each unit flushes.
        self.assertLess(
            source.index("writer.writeheader()"),
            source.index("in as_completed(futures)"),
        )
        self.assertIn("calls_file.flush()", source)
