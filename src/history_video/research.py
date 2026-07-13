"""Research module for gathering event context."""

import os
from pathlib import Path
from typing import Any

from history_video.models import InputRequest


def gather_context(request: InputRequest) -> dict[str, Any]:
    """
    Gather context for the event.

    In offline mode (HISTVIDEO_OFFLINE=1), reads from seeded fixture files.
    Online mode would call OpenRouter API (not implemented).
    """
    offline = os.environ.get("HISTVIDEO_OFFLINE") == "1"

    if offline:
        # Read event title from fixture
        event_title_path = Path("tests/fixtures/history_video/event_title.txt")
        with event_title_path.open("r", encoding="utf-8") as f:
            event_title = f.read().strip()

        # Read supporting doc from fixture
        supporting_doc_path = Path("tests/fixtures/history_video/supporting_doc.txt")
        with supporting_doc_path.open("r", encoding="utf-8") as f:
            supporting_doc = f.read().strip()

        return {
            "event_title": event_title,
            "supporting_doc": supporting_doc,
        }

    # Online mode stub - would call OpenRouter API
    raise NotImplementedError("Online mode not implemented")


__all__ = ["gather_context"]