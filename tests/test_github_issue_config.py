# Copyright (c) 2024-2026 Antonio Trento — https://antoniotrento.net

from __future__ import annotations

import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import github_issue as gh  # noqa: E402


class GithubIssueConfigTests(unittest.TestCase):
    def test_resolve_token_prefers_dotenv_over_process_env(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            env_path = Path(tmp) / ".env"
            env_path.write_text("GITHUB_TOKEN=from-dotenv\n", encoding="utf-8")
            with patch.object(gh, "ENV_FILE", env_path):
                with patch.dict(os.environ, {"GITHUB_TOKEN": "from-process"}, clear=False):
                    self.assertEqual(gh.resolve_token(), "from-dotenv")

    def test_resolve_token_falls_back_to_process_env(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            env_path = Path(tmp) / ".env"
            with patch.object(gh, "ENV_FILE", env_path):
                with patch.dict(os.environ, {"GITHUB_TOKEN": "from-process"}, clear=False):
                    self.assertEqual(gh.resolve_token(), "from-process")

    def test_repo_slug_prefers_dotenv_over_process_env(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            env_path = Path(tmp) / ".env"
            env_path.write_text("GITHUB_REPO=dotenv/repo\n", encoding="utf-8")
            repo_file = Path(tmp) / "github_repo"
            repo_file.write_text("file/repo\n", encoding="utf-8")
            with patch.object(gh, "ENV_FILE", env_path):
                with patch.object(gh, "REPO_FILE", repo_file):
                    with patch.dict(os.environ, {"GITHUB_REPO": "process/repo"}, clear=False):
                        self.assertEqual(gh.repo_slug(), "dotenv/repo")


if __name__ == "__main__":
    unittest.main()
