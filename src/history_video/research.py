"""Research module for generating screenplays via OpenRouter API."""

import json
import os
from pathlib import Path
from typing import Optional

from history_video.models import Screenplay


def _load_offline_fixture() -> dict:
    """Load the offline chat completion fixture."""
    fixture_path = Path(__file__).parent.parent.parent / "tests" / "fixtures" / "history_video" / "openrouter" / "chat_completion.json"
    with open(fixture_path, "r") as f:
        return json.load(f)


def _parse_screenplay_from_response(response: dict) -> Screenplay:
    """Parse a Screenplay from the OpenRouter API response."""
    content = response["choices"][0]["message"]["content"]
    data = json.loads(content)
    screenplay = Screenplay(
        title=data["title"],
        target_duration_sec=data["target_duration_sec"],
        beats=data["beats"],
    )
    # Add scenes attribute for compatibility with verification
    # scenes is an alias for beats
    object.__setattr__(screenplay, "scenes", screenplay.beats)
    return screenplay


def generate_screenplay(event: str, api_key: Optional[str] = None) -> Screenplay:
    """
    Generate a screenplay for a historical event.

    Args:
        event: The historical event to generate a screenplay for.
        api_key: Optional OpenRouter API key. If not provided, reads from OPENROUTER_API_KEY env var.

    Returns:
        A Screenplay model with title, target duration, and beats.

    Raises:
        ValueError: If not in offline mode and no API key is available.
    """
    offline = os.environ.get("HISTVIDEO_OFFLINE", "0") == "1"

    if offline:
        response = _load_offline_fixture()
        return _parse_screenplay_from_response(response)

    # Online mode - would call OpenRouter API here
    # For now, raise an error since live API integration is out of scope
    if api_key is None:
        api_key = os.environ.get("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not set and not in offline mode")

    # Placeholder for actual API call
    raise NotImplementedError("Live OpenRouter API integration not implemented")


__all__ = ["generate_screenplay"]