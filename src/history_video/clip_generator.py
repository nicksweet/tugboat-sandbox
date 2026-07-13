"""Clip generator module for history_video pipeline."""

import os
from pathlib import Path
from typing import List

from history_video.models import ClipSpec


# Fixture clip paths (repo-root relative)
FIXTURE_CLIPS = [
    Path("tests/fixtures/history_video/clips/beat01.mp4"),
    Path("tests/fixtures/history_video/clips/beat02.mp4"),
    Path("tests/fixtures/history_video/clips/beat03.mp4"),
]


def generate_clips(clip_specs: List[ClipSpec]) -> List[Path]:
    """
    Generate clip file paths for the given clip specifications.

    In offline mode (HISTVIDEO_OFFLINE=1), returns seeded fixture clip paths
    in order, cycling if more beats than clips.

    Args:
        clip_specs: List of ClipSpec objects describing each clip to generate.

    Returns:
        List of Path objects pointing to clip files.
    """
    offline = os.environ.get("HISTVIDEO_OFFLINE") == "1"

    if offline:
        # Return fixture clips in order, cycling if needed
        result = []
        for i, _ in enumerate(clip_specs):
            clip_path = FIXTURE_CLIPS[i % len(FIXTURE_CLIPS)]
            result.append(clip_path)
        return result

    # Online mode stub - would call Grok Imagine API
    # For now, raise NotImplementedError to indicate online mode not implemented
    raise NotImplementedError("Online mode (Grok Imagine API) not implemented")


if __name__ == "__main__":
    # Simple test when run directly
    specs = [
        ClipSpec(grok_prompt="p1", beat_id="b1", duration_sec=5.0),
        ClipSpec(grok_prompt="p2", beat_id="b2", duration_sec=7.0),
        ClipSpec(grok_prompt="p3", beat_id="b3", duration_sec=6.0),
    ]
    paths = generate_clips(specs)
    for p in paths:
        print(p)