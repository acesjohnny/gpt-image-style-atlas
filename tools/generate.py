"""Batch-generate the style cards with the Codex CLI's built-in image tool.

One image per style, resumable (finished images are skipped), stops itself after 6 failures in a row
(usually the image quota). Codex runs non-interactively, so it can never approve a paid fallback service.

    python3 tools/generate.py                 # all missing styles, 3 at a time
    python3 tools/generate.py --only 16,88    # just these
    python3 tools/generate.py --model gpt-5.6-sol --workers 2

Output: styles/out/NNN.png, prompts in styles/out/prompts/, one log per attempt in styles/out/logs/.
Requires: `codex` CLI logged in to a ChatGPT plan with image generation.
"""
import argparse, json, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from styles import STYLES, prompt  # noqa: E402

OUT = HERE.parent / "styles" / "out"
PROMPTS, LOGS = OUT / "prompts", OUT / "logs"


def png_complete(path: Path) -> bool:
    try:
        data = path.read_bytes()
        return data[:8] == b"\x89PNG\r\n\x1a\n" and data[-12:-8] == b"\x00\x00\x00\x00" and data[-8:-4] == b"IEND"
    except OSError:
        return False


def run_codex(model: str, prompt_file: Path, out: Path, log: Path, timeout: int) -> bool:
    """Ask Codex to render the prompt file into `out`; stop the CLI as soon as the PNG is complete."""
    instruction = (f"Read the file {prompt_file} and use its entire content verbatim as the image generation prompt. "
                   f"Generate one vertical 3:4 illustration and save it to {out}. Do nothing else and modify no other file.")
    cmd = ["codex", "exec", "-m", model, "-c", "project_doc_max_bytes=0", "-c", "model_reasoning_effort=low",
           "--sandbox", "workspace-write", "--", instruction]
    with log.open("w", encoding="utf-8") as fh:
        proc = subprocess.Popen(cmd, cwd=OUT, stdin=subprocess.DEVNULL, stdout=fh, stderr=subprocess.STDOUT)
        deadline, stable_since, last = time.time() + timeout, None, -1
        while proc.poll() is None:
            if time.time() > deadline:
                proc.kill(); break
            size = out.stat().st_size if out.is_file() else -1
            if size > 0 and size == last and png_complete(out):
                stable_since = stable_since or time.time()
                if time.time() - stable_since > 2:
                    proc.terminate(); break
            last = size
            time.sleep(1)
    return out.is_file() and out.stat().st_size > 50_000


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--model", default="gpt-5.6-sol", help="Codex text model that drives the image tool")
    ap.add_argument("--timeout", type=int, default=900)
    args = ap.parse_args()
    for d in (OUT, PROMPTS, LOGS):
        d.mkdir(parents=True, exist_ok=True)
    only = {int(x) for x in args.only.split(",") if x}
    state, lock = {"streak": 0, "stop": False}, threading.Lock()

    def job(n):
        _, name, _ = STYLES[n - 1]
        out = OUT / f"{n:03d}.png"
        if out.exists() or state["stop"]:
            return
        pf = PROMPTS / f"{n:03d}.md"
        pf.write_text(f"# {n:03d} {name}\n\n" + prompt(STYLES[n - 1]), encoding="utf-8")
        for attempt in (1, 2):
            t0 = time.time()
            ok = run_codex(args.model, pf, out, LOGS / f"{n:03d}-try{attempt}.log", args.timeout)
            with lock:
                print(f"{time.strftime('%H:%M:%S')} {n:03d} {name} {'OK' if ok else 'FAIL'} try{attempt} {time.time()-t0:.0f}s",
                      flush=True)
                if ok:
                    state["streak"] = 0
                    return
                state["streak"] += 1
                if state["streak"] >= 6:
                    state["stop"] = True
                    print("6 failures in a row - stopping (image quota or network). Re-run later to resume.", flush=True)
                    return

    todo = [n for n in range(1, len(STYLES) + 1) if not only or n in only]
    with ThreadPoolExecutor(args.workers) as ex:
        list(ex.map(job, todo))
    print(f"done: {len(list(OUT.glob('*.png')))}/{len(STYLES)}")


if __name__ == "__main__":
    main()
