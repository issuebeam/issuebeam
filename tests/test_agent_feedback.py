# Copyright (c) 2024-2026 Antonio Trento — https://antoniotrento.net

from __future__ import annotations

import argparse
import io
import json
import os
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import MagicMock, patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import agent_feedback as af  # noqa: E402


class AgentFeedbackTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmpdir = tempfile.TemporaryDirectory()
        self.state_path = Path(self._tmpdir.name) / "state.json"
        os.environ["ISSUEBEAM_FEEDBACK_STATE_FILE"] = str(self.state_path)
        os.environ.pop("DO_NOT_TRACK", None)
        os.environ.pop("CI", None)

    def tearDown(self) -> None:
        self._tmpdir.cleanup()
        os.environ.pop("ISSUEBEAM_FEEDBACK_STATE_FILE", None)

    def test_count_only_on_backlog_commands(self) -> None:
        with patch.object(sys.stdout, "isatty", return_value=True):
            for _ in range(49):
                af.after_success("create")
            state = json.loads(self.state_path.read_text(encoding="utf-8"))
            self.assertEqual(state["count"], 49)

            af.after_success("create")
            state = json.loads(self.state_path.read_text(encoding="utf-8"))
            self.assertEqual(state["count"], 50)

            before = state["count"]
            for _ in range(100):
                af.after_success("list")
            after = json.loads(self.state_path.read_text(encoding="utf-8"))
            self.assertEqual(after["count"], before)

    def test_note_at_threshold(self) -> None:
        with patch.object(sys.stdout, "isatty", return_value=True):
            captured = io.StringIO()
            with patch("sys.stdout", new=captured):
                with patch.object(captured, "isatty", return_value=True):
                    for _ in range(50):
                        af.after_success("create")
            output = captured.getvalue()
            self.assertIn("issuebeam: optional maintainer note (usage #50)", output)
            self.assertIn("feedback --decline", output)

    def test_decline_no_api_call(self) -> None:
        args = argparse.Namespace(
            decline=True,
            message="",
            email="",
            subscribe=False,
            locale="",
        )
        with patch.object(af, "post_intake") as mock_post:
            code = af.cmd_feedback(args)
        self.assertEqual(code, 0)
        mock_post.assert_not_called()
        state = json.loads(self.state_path.read_text(encoding="utf-8"))
        self.assertEqual(state["status"], "declined")

    def test_feedback_success_marks_completed(self) -> None:
        args = argparse.Namespace(
            decline=False,
            message="thanks",
            email="",
            subscribe=False,
            locale="",
        )
        with patch.object(af, "post_intake", return_value=True):
            code = af.cmd_feedback(args)
        self.assertEqual(code, 0)
        state = json.loads(self.state_path.read_text(encoding="utf-8"))
        self.assertEqual(state["status"], "completed")

    def test_feedback_api_down_keeps_active(self) -> None:
        af.save_state(af.default_state())
        args = argparse.Namespace(
            decline=False,
            message="thanks",
            email="",
            subscribe=False,
            locale="",
        )
        with patch.object(af, "post_intake", return_value=False):
            code = af.cmd_feedback(args)
        self.assertEqual(code, 1)
        state = json.loads(self.state_path.read_text(encoding="utf-8"))
        self.assertEqual(state["status"], "active")

    def test_subscribe_payload(self) -> None:
        args = argparse.Namespace(
            decline=False,
            message="",
            email="user@example.com",
            subscribe=True,
            locale="en",
        )
        with patch.object(af, "post_intake", return_value=True) as mock_post:
            af.cmd_feedback(args)
        payload = mock_post.call_args[0][0]
        self.assertEqual(payload["kind"], "subscribe")
        self.assertEqual(payload["email"], "user@example.com")
        self.assertTrue(payload["consent"])

    def test_declined_cooldown_blocks_increment(self) -> None:
        declined_at = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
        af.save_state(
            {
                "count": 10,
                "status": "declined",
                "declined_at": declined_at,
                "completed_at": None,
            }
        )
        with patch.object(sys.stdout, "isatty", return_value=True):
            count = af.bump_count()
        self.assertEqual(count, 10)
        state = json.loads(self.state_path.read_text(encoding="utf-8"))
        self.assertEqual(state["count"], 10)


if __name__ == "__main__":
    unittest.main()
