"""Tests for CLI entry point."""

import os
import subprocess
import tempfile
from pathlib import Path

import pytest
from typer.testing import CliRunner

from history_video.cli import app


@pytest.fixture(autouse=True)
def offline_mode():
    """Ensure offline mode is set for all tests."""
    os.environ["HISTVIDEO_OFFLINE"] = "1"
    yield
    # Clean up if needed
    if "HISTVIDEO_OFFLINE" in os.environ:
        del os.environ["HISTVIDEO_OFFLINE"]


def test_cli_generate_command_exists():
    """Test that the generate command exists and shows help."""
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "generate" in result.output
    assert "event-title" in result.output.lower() or "event_title" in result.output.lower()


def test_cli_generate_help():
    """Test generate command help."""
    runner = CliRunner()
    result = runner.invoke(app, ["generate", "--help"])
    assert result.exit_code == 0
    assert "--out" in result.output
    assert "--genre" in result.output
    assert "--role" in result.output


def test_cli_generate_offline_smoke():
    """Test CLI generate command in offline mode produces valid MP4."""
    runner = CliRunner()

    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as f:
        out_path = Path(f.name)

    try:
        # Single-command app: invoke with positional event title first
        result = runner.invoke(app, [
            "Test Event",
            "--genre", "documentary",
            "--role", "narrator",
            "--out", str(out_path)
        ])

        print(f"Exit code: {result.exit_code}")
        print(f"Output: {result.output}")

        assert result.exit_code == 0, f"CLI failed: {result.output}"
        assert out_path.exists(), "Output MP4 not created"
        assert out_path.stat().st_size > 0, "Output file empty"

        # Verify video duration using ffprobe
        dur_output = subprocess.check_output([
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(out_path)
        ]).decode().strip()

        duration = float(dur_output)
        assert duration > 0, f"Duration {duration} not > 0"

        print(f"CLI smoke test OK: {out_path} {duration:.2f}s")

    finally:
        # Clean up
        if out_path.exists():
            out_path.unlink()


def test_cli_missing_out_option():
    """Test that --out is required."""
    runner = CliRunner()
    result = runner.invoke(app, ["Test Event"])
    assert result.exit_code != 0
    assert "Missing option" in result.output or "required" in result.output.lower()


def test_cli_invalid_event_title():
    """Test with empty event title."""
    runner = CliRunner()
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as f:
        out_path = Path(f.name)

    try:
        result = runner.invoke(app, ["", "--out", str(out_path)])
        # Empty string as argument might be handled differently
        # Just verify it doesn't crash unexpectedly
        assert result.exit_code in (0, 2)  # 0 = success, 2 = usage error
    finally:
        if out_path.exists():
            out_path.unlink()