"""Check in a real browser that each answer on the marking page reaches the file.

The node tests cover the server only. This check clicks the page in headless
Chrome against a blank copy of a sheet, then reads the copy back from disk.
Run it with `task marking-check` before anyone marks a sheet.
"""

import asyncio
import csv
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request

import websockets

APP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.environ.get("MARKING_SOURCE_REPO", os.path.dirname(os.path.dirname(APP)))
CHROME = os.environ.get(
    "CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
)
PORT = 5179
DEBUG_PORT = 9339


def blank_copy(sheet, work):
    """Copy a sheet folder with every mark and note blank."""
    src = os.path.join(REPO, "tests/evaluation/results", sheet)
    dst = os.path.join(work, "tests/evaluation/results", sheet)
    os.makedirs(dst)
    shutil.copy(os.path.join(src, "items.json"), dst)
    with open(os.path.join(src, "sheet.csv")) as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["domain_right_human"] = r["reason_cause_effect_human"] = r["note"] = ""
    with open(os.path.join(dst, "sheet.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return os.path.join(dst, "sheet.csv")


def file_row(path, i):
    with open(path) as f:
        r = list(csv.DictReader(f))[i]
    return r["domain_right_human"], r["reason_cause_effect_human"]


def wait_http(url, tries=100):
    for _ in range(tries):
        try:
            return urllib.request.urlopen(url, timeout=1).read()
        except OSError:
            time.sleep(0.2)
    raise SystemExit(f"no answer from {url}")


async def drive(sheet_path):
    n = 0
    tabs = json.loads(wait_http(f"http://127.0.0.1:{DEBUG_PORT}/json"))
    ws_url = next(t for t in tabs if t["type"] == "page")["webSocketDebuggerUrl"]
    async with websockets.connect(ws_url, max_size=None) as ws:

        async def js(expr):
            nonlocal n
            n += 1
            await ws.send(
                json.dumps(
                    {
                        "id": n,
                        "method": "Runtime.evaluate",
                        "params": {
                            "expression": expr,
                            "awaitPromise": True,
                            "returnByValue": True,
                        },
                    }
                )
            )
            while True:
                msg = json.loads(await ws.recv())
                if msg.get("id") == n:
                    return msg.get("result", {}).get("result", {}).get("value")

        async def key(k):
            await js(
                f"window.dispatchEvent(new KeyboardEvent('keydown', {{key: '{k}'}}))"
            )

        n += 1
        await ws.send(
            json.dumps(
                {
                    "id": n,
                    "method": "Page.navigate",
                    "params": {"url": f"http://localhost:{PORT}/"},
                }
            )
        )
        for _ in range(50):
            if await js("document.querySelector('h1')?.textContent") == "Blind marking":
                break
            await asyncio.sleep(0.2)
        # The server sends the page before its scripts run; keys only work once they do.
        for _ in range(100):
            if await js("document.documentElement.dataset.ready === 'true'"):
                break
            await asyncio.sleep(0.1)
        else:
            raise SystemExit("the page never became ready")

        # Each case: the keys pressed on row 1, then the marks the file must hold.
        cases = [
            (["1"], ("True", "")),
            (["4"], ("True", "False")),
            (["3"], ("True", "True")),
            (["3"], ("True", "")),  # a second press clears the answer
            (["2", "3"], ("False", "True")),  # two fast keys
        ]
        failures = 0
        for keys, want in cases:
            for k in keys:
                await key(k)
            await asyncio.sleep(1.5)
            got = file_row(sheet_path, 0)
            status = await js("document.querySelector('header p').textContent")
            ok = got == want and status.endswith("Saved")
            failures += not ok
            print(
                f"{'ok  ' if ok else 'FAIL'} keys {'+'.join(keys)}: file {got}, want {want}, page says {status!r}"
            )
        return failures


def main():
    sheet = sys.argv[1] if len(sys.argv) > 1 else "2026-11-05-human-marking"
    work = tempfile.mkdtemp(prefix="marking-check-")
    sheet_path = blank_copy(sheet, work)
    env = {**os.environ, "MARKING_REPO": work, "MARKING_SHEET": sheet}
    vite = subprocess.Popen(
        [
            os.path.join(APP, "node_modules/.bin/vite"),
            "dev",
            "--port",
            str(PORT),
            "--strictPort",
        ],
        cwd=APP,
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    chrome = None
    try:
        wait_http(f"http://localhost:{PORT}/")
        chrome = subprocess.Popen(
            [
                CHROME,
                "--headless=new",
                f"--remote-debugging-port={DEBUG_PORT}",
                f"--user-data-dir={work}/chrome",
                "--no-first-run",
                "about:blank",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        failures = asyncio.run(drive(sheet_path))
    finally:
        for p in (chrome, vite):
            if p:
                p.terminate()
                p.wait()
        shutil.rmtree(work, ignore_errors=True)
    print("browser save check:", "passed" if not failures else f"{failures} failed")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
