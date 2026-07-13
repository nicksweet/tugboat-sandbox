"""Clip generator module for producing video clips from ClipDescription objects."""

import os
from pathlib import Path
from typing import List

from history_video.models import ClipDescription


def generate_clips(descriptions: List[ClipDescription]) -> List[Path]:
    """
    Generate video clips from ClipDescription objects.

    In offline mode (HISTVIDEO_OFFLINE=1), returns paths to seeded fixture clips.
    """
    offline = os.environ.get("HISTVIDEO_OFFLINE") == "1"

    if offline:
        # Return paths to the three seeded fixture clips
        fixture_dir = Path("tests/fixtures/history_video/clips")
        fixture_clips = [
            fixture_dir / "beat01.mp4",
            fixture_dir / "beat02.mp4",
            fixture_dir / "beat03.mp4",
        ]
        # Verify fixtures exist
        for clip in fixture_clips:
            if not clip.exists():
                raise FileNotFoundError(f"Fixture clip not found: {clip}")
        return fixture_clips

    # Online mode - would integrate with Grok Imagine API
    # For now, raise NotImplementedError
    raise NotImplementedError("Online clip generation not implemented")


__all__ = ["generate_clips"]