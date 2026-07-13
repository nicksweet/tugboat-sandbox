"""Tests for clip_generator module."""

import os
from pathlib import Path

import pytest

from history_video.clip_generator import generate_clips
from history_video.models import ClipDescription


def test_generate_clips_offline_returns_fixture_paths():
    """Test that offline mode returns paths to seeded fixture clips."""
    # Ensure offline mode is set
    os.environ["HISTVIDEO_OFFLINE"] = "1"

    # Create dummy clip descriptions
    descs = [
        ClipDescription(
            id="clip_1",
            description="Scene 1",
            duration_seconds=5.0,
            visual_prompt="v1",
            audio_prompt="a1",
            start_time=0.0,
            end_time=5.0,
        ),
        ClipDescription(
            id="clip_2",
            description="Scene 2",
            duration_seconds=5.0,
            visual_prompt="v2",
            audio_prompt="a2",
            start_time=5.0,
            end_time=10.0,
        ),
        ClipDescription(
            id="clip_3",
            description="Scene 3",
            duration_seconds=5.0,
            visual_prompt="v3",
            audio_prompt="a3",
            start_time=10.0,
            end_time=15.0,
        ),
    ]

    paths = generate_clips(descs)

    # Verify return type and count
    assert isinstance(paths, list), "Expected list of paths"
    assert len(paths) == 3, f"Expected 3 paths, got {len(paths)}"

    # Verify each path is a Path object and exists
    for p in paths:
        assert isinstance(p, Path), f"Not Path: {type(p)}"
        assert p.exists(), f"Fixture not found: {p}"
        assert p.name.startswith("beat"), f"Unexpected fixture: {p.name}"

    # Verify specific fixture names
    names = [p.name for p in paths]
    assert "beat01.mp4" in names
    assert "beat02.mp4" in names
    assert "beat03.mp4" in names


def test_generate_clips_online_raises_not_implemented():
    """Test that online mode raises NotImplementedError."""
    # Ensure offline mode is NOT set
    os.environ.pop("HISTVIDEO_OFFLINE", None)

    descs = [
        ClipDescription(
            id="clip_1",
            description="Scene 1",
            duration_seconds=5.0,
            visual_prompt="v1",
            audio_prompt="a1",
            start_time=0.0,
            end_time=5.0,
        ),
    ]

    with pytest.raises(NotImplementedError):
        generate_clips(descs)