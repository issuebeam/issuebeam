#!/usr/bin/env python3
"""Copy issuebeam skeleton into another project (Windows-safe, pathlib + shutil)."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Relative paths inside this skeleton repo → same path in target repo
COPY_PATHS = [
    "scripts/github_issue.py",
    "tracker/labels.yml",
    "tracker/README.md",
    "tracker/import-manifest.example.json",
    "tracker/github_repo.example",
    "tracker/github_token.example",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/ISSUE_TEMPLATE/task.yml",
    ".github/copilot-instructions.md",
    ".cursor/rules/github-issues.mdc",
    "AGENTS.md",
    "CLAUDE.md",
]


def validate_repo_slug(slug: str) -> str:
    slug = slug.strip()
    if "/" not in slug or slug.count("/") != 1:
        print(f"ERRORE: --repo deve essere owner/repo, ricevuto: {slug!r}", file=sys.stderr)
        sys.exit(1)
    owner, name = slug.split("/", 1)
    if not owner or not name:
        print(f"ERRORE: --repo non valido: {slug!r}", file=sys.stderr)
        sys.exit(1)
    return slug


def copy_file(src: Path, dst: Path, *, force: bool) -> None:
    if dst.exists() and not force:
        print(f"  SALTATO (esiste): {dst}")
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"  COPIATO: {dst}")


def adopt(target: Path, repo: str, *, force: bool = False) -> None:
    target = target.resolve()
    if not target.is_dir():
        print(f"ERRORE: directory target non trovata: {target}", file=sys.stderr)
        sys.exit(1)

    print(f"Adozione issuebeam in: {target}")
    print(f"Repository GitHub: {repo}")
    print()

    for rel in COPY_PATHS:
        src = ROOT / rel
        if not src.is_file():
            print(f"ERRORE: file sorgente mancante nello skeleton: {src}", file=sys.stderr)
            sys.exit(1)
        dst = target / rel
        copy_file(src, dst, force=force)

    # tracker/github_repo — always written (repo slug)
    repo_file = target / "tracker" / "github_repo"
    if repo_file.exists() and not force:
        print(f"  SALTATO (esiste): {repo_file}")
    else:
        repo_file.parent.mkdir(parents=True, exist_ok=True)
        repo_file.write_text(repo + "\n", encoding="utf-8")
        print(f"  SCRITTO: {repo_file}")

    # Optional: seed import-manifest.json from example if missing
    manifest = target / "tracker" / "import-manifest.json"
    example = target / "tracker" / "import-manifest.example.json"
    if not manifest.exists() and example.is_file():
        shutil.copy2(example, manifest)
        print(f"  CREATO: {manifest} (da example)")

    # .secrets/ placeholder (gitignored)
    secrets_dir = target / ".secrets"
    secrets_dir.mkdir(parents=True, exist_ok=True)
    gitkeep = secrets_dir / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.write_text("", encoding="utf-8")
        print(f"  CREATO: {gitkeep}")

    print()
    print("Fatto. Prossimi passi:")
    print("  1. Configura GITHUB_TOKEN (env, .env o .secrets/github_token — vedi docs/getting-started/token)")
    print("  2. python scripts/github_issue.py labels --apply")
    print("  3. Apri il progetto nel tuo agente AI (Cursor, Claude Code, Copilot, …)")
    print("     - Cursor: .cursor/rules/github-issues.mdc")
    print("     - Claude Code: CLAUDE.md + AGENTS.md")
    print("     - Copilot: .github/copilot-instructions.md + AGENTS.md")
    print("     - Altre piattaforme: https://issuebeam.github.io/docs/platforms/overview/")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Copia lo skeleton issuebeam in un altro repository.",
    )
    parser.add_argument(
        "--target",
        required=True,
        help="Directory del progetto destinazione (es. ../my-repo)",
    )
    parser.add_argument(
        "--repo",
        required=True,
        help="Slug GitHub owner/repo (es. myorg/my-app)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Sovrascrive file già presenti",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    target = Path(args.target)
    repo = validate_repo_slug(args.repo)
    adopt(target, repo, force=args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
