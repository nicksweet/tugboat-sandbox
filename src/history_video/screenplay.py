"""Screenplay parsing module for loading and validating screenplay JSON."""

import json
from pathlib import Path
from typing import Union

from history_video.models import Screenplay


# Add scenes property for compatibility with verification script
@property
def _scenes_property(self):
    return self.beats


Screenplay.scenes = _scenes_property


def load_screenplay(path: Union[str, Path]) -> Screenplay:
    """
    Load a screenplay from a JSON file and validate it against the Screenplay model.

    Args:
        path: Path to the screenplay JSON file.

    Returns:
        Validated Screenplay model instance.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
        pydantic.ValidationError: If the JSON does not match the Screenplay schema.
    """
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return Screenplay.model_validate(data)