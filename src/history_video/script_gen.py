import json
import os
from .models import Beat, Screenplay


def generate_screenplay(title: str, doc_paths: list[str] | None = None, *, offline: bool = False) -> Screenplay:
    """Generate a screenplay for a historical video.

    Args:
        title: Title of the video.
        doc_paths: Optional list of document paths (unused in offline mode).
        offline: If True, load beats from offline fixture. Also respects
            HISTVIDEO_OFFLINE=1 environment variable.

    Returns:
        A Screenplay instance.
    """
    # Determine if we should use offline mode
    if offline or os.environ.get('HISTVIDEO_OFFLINE') == '1':
        fixture_path = 'tests/fixtures/history_video/screenplay.json'
        with open(fixture_path, 'r') as f:
            data = json.load(f)
        # Convert beat dictionaries to Beat instances
        beats = [Beat(**beat_data) for beat_data in data['beats']]
        # Use the provided title, but keep target_duration_sec from fixture if present
        return Screenplay(
            title=title,
            beats=beats,
            target_duration_sec=data.get('target_duration_sec', 150.0)
        )
    else:
        # Online mode (live LLM or doc-fetch) is out of scope for this task.
        # Return an empty screenplay as a placeholder.
        return Screenplay(title=title, beats=[], target_duration_sec=0.0)