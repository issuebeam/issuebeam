#!/usr/bin/env python3
"""Publish MkDocs to issuebeam.github.io (Pages repo sibling clone)."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "docs" / "requirements.txt"
PAGES_REPO = ROOT.parent / "issuebeam.github.io"
PAGES_SUBDIR = "docs"


def run(cmd: list[str], *, cwd: Path | None = None) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd or ROOT, check=True)


def main() -> int:
    print("=== Issuebeam — publish documentation ===\n")
    pages_repo = PAGES_REPO
    if not pages_repo.is_dir():
        print(f"[FAIL] Pages repo folder not found: {pages_repo}")
        print("\nOne-time setup (sibling folder next to this repo):")
        print(f"  cd {ROOT.parent}")
        print("  git clone https://github.com/issuebeam/issuebeam.github.io.git")
        return 1

    has_git = (pages_repo / ".git").is_dir()
    if not has_git:
        print(f"[WARN] No git in {pages_repo} — will copy HTML only (no commit).\n")

    run([sys.executable, "-m", "pip", "install", "-r", str(REQ)])

    build_dir = Path(tempfile.mkdtemp(prefix="issuebeam_docs_"))
    try:
        print(f"\n[1/3] mkdocs build -> {build_dir}")
        run([sys.executable, "-m", "mkdocs", "build", "-d", str(build_dir)])

        target = pages_repo / PAGES_SUBDIR
        print(f"[2/3] Copy -> {target}")
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(build_dir, target)

        if not has_git:
            print("\n[OK] Documentation copied (no git commit).")
            print("Site: https://issuebeam.github.io/docs/")
            return 0

        print(f"[3/3] git commit in {pages_repo}")
        run(["git", "add", PAGES_SUBDIR], cwd=pages_repo)
        status = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=pages_repo,
        )
        if status.returncode == 0:
            print("[OK] No documentation changes.")
            return 0

        run(
            ["git", "commit", "-m", "docs: update Issuebeam documentation"],
            cwd=pages_repo,
        )
    finally:
        shutil.rmtree(build_dir, ignore_errors=True)

    print("\n[OK] Commit created in issuebeam.github.io")
    print(f"To publish: cd {pages_repo} && git push")
    print("Site: https://issuebeam.github.io/docs/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
