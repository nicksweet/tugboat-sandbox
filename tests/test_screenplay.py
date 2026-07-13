"""Tests for screenplay parsing module."""

import os
import sys

# Ensure offline mode for tests
os.environ["HISTVIDEO_OFFLINE"] = "1"

# Add src to path for imports
sys.path.insert(0, "src")

import pytest
from history_video.screenplay import load_screenplay
from history_video.models import Screenplay


def test_load_screenplay_fixture():
    """Test loading the offline screenplay fixture."""
    screenplay = load_screenplay("tests/fixtures/history_video/screenplay.json")

    # Verify it's a Screenplay model
    assert isinstance(screenplay, Screenplay), f"Expected Screenplay, got {type(screenplay)}"

    # Verify required fields
    assert screenplay.title != "", "Empty title"
    assert screenplay.title == "Moon Landing 1969"
    assert screenplay.target_duration_sec == 150.0

    # Verify beats
    assert len(screenplay.beats) > 0, "No scenes"
    assert len(screenplay.beats) == 3

    # Verify first beat
    beat1 = screenplay.beats[0]
    assert beat1.order == 1
    assert beat1.slug == "launch-pad"
    assert "Saturn V" in beat1.action
    assert beat1.duration_sec == 50.0

    # Verify second beat
    beat2 = screenplay.beats[1]
    assert beat2.order == 2
    assert beat2.slug == "lunar-descent"
    assert "Eagle" in beat2.action
    assert beat2.duration_sec == 50.0

    # Verify third beat
    beat3 = screenplay.beats[2]
    assert beat3.order == 3
    assert beat3.slug == "first-step"
    assert "lunar dust" in beat3.action
    assert beat3.duration_sec == 50.0


def test_load_screenplay_invalid_path():
    """Test that loading a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        load_screenplay("tests/fixtures/history_video/nonexistent.json")


def test_load_screenplay_invalid_json():
    """Test that loading invalid JSON raises JSONDecodeError."""
    import tempfile
    import json

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        f.write("{ invalid json }")
        temp_path = f.name

    try:
        with pytest.raises(json.JSONDecodeError):
            load_screenplay(temp_path)
    finally:
        os.unlink(temp_path)


def test_load_screenplay_invalid_schema():
    """Test that loading JSON with invalid schema raises ValidationError."""
    import tempfile
    import json
    from pydantic import ValidationError

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump({"title": "Test"}, f)  # Missing required fields
        temp_path = f.name

    try:
        with pytest.raises(ValidationError):
            load_screenplay(temp_path)
    finally:
        os.unlink(temp_path)