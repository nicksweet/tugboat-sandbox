"""Screenplay generation module for history_video pipeline."""

import json
import os
from pathlib import Path
from typing import Any

from history_video.models import Beat, InputRequest, Screenplay


def _load_offline_screenplay() -> Screenplay:
    """Load and parse the offline screenplay fixture."""
    fixture_path = Path("tests/fixtures/history_video/screenplay.json")
    with fixture_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    beats = []
    for beat_data in data.get("beats", []):
        beat = Beat(
            id=beat_data.get("slug", ""),
            narration=beat_data.get("action", ""),
            visual_description=beat_data.get("action", ""),
            duration_sec=beat_data.get("duration_sec", 0.0),
        )
        beats.append(beat)

    return Screenplay(beats=beats)


def generate_screenplay(context: dict[str, Any], request: InputRequest) -> Screenplay:
    """
    Generate a beat-sheet guided screenplay.

    In offline mode (HISTVIDEO_OFFLINE=1), loads the seeded fixture.
    Online mode would call OpenRouter API (not implemented).
    """
    offline = os.environ.get("HISTVIDEO_OFFLINE") == "1"

    if offline:
        return _load_offline_screenplay()

    # Online mode stub - would call OpenRouter API
    raise NotImplementedError("Online mode not implemented")