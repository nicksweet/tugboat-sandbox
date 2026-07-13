"""Tests for the assemble module."""

import subprocess
import tempfile
from pathlib import Path

import pytest

from history_video.assemble import assemble_clips


def test_assemble_clips_creates_valid_mp4():
    """Test that assemble_clips produces a valid MP4 with duration > 0."""
    clips = [
        Path("tests/fixtures/history_video/clips/beat01.mp4"),
        Path("tests/fixtures/history_video/clips/beat02.mp4"),
        Path("tests/fixtures/history_video/clips/beat03.mp4"),
    ]

    # Verify all fixture clips exist
    for clip in clips:
        assert clip.exists(), f"Missing fixture: {clip}"

    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as f:
        output_path = Path(f.name)

    try:
        assemble_clips(clips, output_path)

        # Verify output exists and is non-empty
        assert output_path.exists(), "Output MP4 not created"
        assert output_path.stat().st_size > 0, "Output file empty"

        # Verify duration > 0 using ffprobe
        dur_output = subprocess.check_output(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "default=noprint_wrappers=1:nokey=1",
                str(output_path),
            ],
            text=True,
        ).strip()
        duration = float(dur_output)
        assert duration > 0, f"Duration {duration} not > 0"

    finally:
        # Clean up
        if output_path.exists():
            output_path.unlink()


def test_assemble_clips_empty_list_raises():
    """Test that empty clip list raises ValueError."""
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as f:
        output_path = Path(f.name)

    try:
        with pytest.raises(ValueError, match="No clip paths provided"):
            assemble_clips([], output_path)
    finally:
        if output_path.exists():
            output_path.unlink()