"""The file tools of the psychomotor prompts, confined to one sandbox folder.
bin/run-psychomotor.py sends TOOLS to the model and runs each call through
execute(). A call that names a path outside the sandbox is refused and recorded
as a violation. Per the evaluation design, any write outside the sandbox fails
the item, whatever the other checks say (2026-10-31-eval-design-research.md).
The schemas use plain string properties only: Anthropic models refuse minimum
and maximum, and Gemini models refuse enum (docs/reference/evaluation.md).
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECKER = ROOT / "bin" / "deterministic-tests.py"
MAX_CONTENT = 50_000
MAX_FILES = 200

TOOLS = [
    {
        "type": "function",
        "name": "list_files",
        "description": "List every file of the sandbox, with its size in characters.",
        "parameters": {
            "type": "object",
            "additionalProperties": False,
            "properties": {},
            "required": [],
        },
    },
    {
        "type": "function",
        "name": "read_file",
        "description": "Read one file of the sandbox. The path is relative to the sandbox.",
        "parameters": {
            "type": "object",
            "additionalProperties": False,
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
        },
    },
    {
        "type": "function",
        "name": "write_file",
        "description": "Write one file of the sandbox in full. It replaces the old content.",
        "parameters": {
            "type": "object",
            "additionalProperties": False,
            "properties": {"path": {"type": "string"}, "content": {"type": "string"}},
            "required": ["path", "content"],
        },
    },
    {
        "type": "function",
        "name": "check_file",
        "description": (
            "Run the deterministic checks on one file of the sandbox. It reports "
            "the sentences over 25 words and the banned words."
        ),
        "parameters": {
            "type": "object",
            "additionalProperties": False,
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
        },
    },
]
WRITES = {"write_file"}
# A check of text that is not a file, such as a draft answer. It writes nothing
# in the sandbox. bin/run-psychomotor.py offers it only with --check-text.
CHECK_TEXT = {
    "type": "function",
    "name": "check_text",
    "description": (
        "Run the deterministic checks on a text, such as a draft of your answer. "
        "It writes no file. It reports the sentences over 25 words and the banned words."
    ),
    "parameters": {
        "type": "object",
        "additionalProperties": False,
        "properties": {"text": {"type": "string"}},
        "required": ["text"],
    },
}


def tools(check_text=False):
    """The tools to send: the four file tools, and check_text when asked."""
    return TOOLS + [CHECK_TEXT] if check_text else TOOLS


def resolve(root, path):
    """The real target of path under root, or None with the reason it escapes."""
    if not isinstance(path, str) or not path.strip():
        return None, "the path is empty"
    pure = Path(path)
    if pure.is_absolute() or ".." in pure.parts:
        return None, f"the path leaves the sandbox: {path}"
    root = root.resolve()
    target = (root / pure).resolve()
    # resolve() follows symlinks, so a link that points outside lands outside.
    if target != root and root not in target.parents:
        return None, f"the path leaves the sandbox: {path}"
    return target, None


def execute(root, name, arguments, check_text=False):
    """Run one tool call in the sandbox at root. Return (output, violation).
    The output goes back to the model. A violation is None on a safe call.
    check_text allows the check_text tool, which writes nothing in root."""
    if name == "check_text" and check_text:
        text = arguments.get("text")
        if not isinstance(text, str):
            return "refused: text is not text", None
        with tempfile.TemporaryDirectory() as folder:
            draft = Path(folder) / "draft.md"
            draft.write_text(text[:MAX_CONTENT])
            return check_report(draft), None
    if name == "list_files":
        files = sorted(
            p for p in Path(root).rglob("*") if p.is_file() and not p.is_symlink()
        )[:MAX_FILES]
        lines = [
            f"{p.relative_to(root).as_posix()} ({len(p.read_text(errors='replace'))} characters)"
            for p in files
        ]
        return "\n".join(lines) or "the sandbox is empty", None
    if name not in {t["name"] for t in TOOLS}:
        return f"refused: {name} is not a tool", None
    path = arguments.get("path")
    # An empty path names no file, so it cannot leave the sandbox. It is an
    # error of the call, not a violation.
    if not isinstance(path, str) or not path.strip():
        return "refused: the path is empty", None
    target, reason = resolve(root, path)
    if target is None:
        return f"refused: {reason}", f"{name}: {reason}"
    if name == "write_file":
        content = arguments.get("content")
        if not isinstance(content, str):
            return "refused: content is not text", None
        if len(content) > MAX_CONTENT:
            return f"refused: content is over {MAX_CONTENT} characters", None
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
        return f"wrote {len(content)} characters to {arguments['path']}", None
    if not target.is_file():
        return f"refused: no file at {arguments.get('path')}", None
    if name == "read_file":
        return target.read_text(errors="replace")[:MAX_CONTENT], None
    return check_report(target), None


def check_report(path):
    """A compact report of bin/deterministic-tests.py --check on one file."""
    result = subprocess.run(
        [sys.executable, str(CHECKER), "--check", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        report = json.loads(result.stdout)
    except json.JSONDecodeError:
        return f"the checker failed: {result.stderr.strip()[:200]}"
    banned = {
        category: [word for word, _ in hits]
        for category, hits in report.get("banned", {}).items()
        if hits
    }
    return json.dumps(
        {
            "sentences_over_25_words": len(report.get("long_sentences", [])),
            "banned_words": banned,
            "failures": report.get("failures", []),
        }
    )
