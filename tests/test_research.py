"""Tests for the research module."""

import os
import sys

# Ensure src is in path
sys.path.insert(0, "src")

import pytest

from history_video.research import generate_screenplay
from history_video.models import Screenplay


def test_generate_screenplay_offline_mode():
    """Test that generate_screenplay loads fixture in offline mode."""
    # Set offline mode
    os.environ["HISTVIDEO_OFFLINE"] = "1"

    try:
        screenplay = generate_screenplay("Test Event", None)

        # Verify it returns a Screenplay model
        assert isinstance(screenplay, Screenplay), f"Expected Screenplay, got {type(screenplay)}"

        # Verify required fields
        assert hasattr(screenplay, "title"), "Missing title field"
        assert hasattr(screenplay, "target_duration_sec"), "Missing target_duration_sec field"
        assert hasattr(screenplay, "beats"), "Missing beats field"

        # Verify content from fixture
        assert screenplay.title == "Moon Landing 1969"
        assert screenplay.target_duration_sec == 150.0
        assert len(screenplay.beats) == 6

        # Verify beat structure
        for i, beat in enumerate(screenplay.beats):
            assert beat.order == i + 1
            assert beat.slug
            assert beat.action
            assert beat.duration_sec == 25.0

        print("Research module OK:", screenplay.title, len(screenplay.beats), "scenes")
    finally:
        # Clean up
        os.environ.pop("HISTVIDEO_OFFLINE", None)


def test_generate_screenplay_requires_api_key_when_online():
    """Test that online mode requires API key."""
    # Ensure offline mode is disabled
    os.environ["HISTVIDEO_OFFLINE"] = "0"
    os.environ.pop("OPENROUTER_API_KEY", None)

    try:
        with pytest.raises(ValueError, match="OPENROUTER_API_KEY not set"):
            generate_screenplay("Test Event", None)
    finally:
        os.environ.pop("HISTVIDEO_OFFLINE", None)


if __name__ == "__main__":
    test_generate_screenplay_offline_mode()
    test_generate_screenplay_requires_api_key_when_online()
    print("All tests passed!")