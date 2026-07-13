"""Domain models for history_video pipeline."""

from pathlib import Path
from typing import List, Optional

from pydantic import BaseModel, Field


class InputRequest(BaseModel):
    """Input request for the history video pipeline."""
    event_title: str
    genre: str
    role: str
    supporting_docs: List[Path] = Field(default_factory=list)


class Beat(BaseModel):
    """A single beat in the screenplay."""
    id: str
    narration: str
    visual_description: str
    duration_sec: float


class Screenplay(BaseModel):
    """Complete screenplay composed of beats."""
    beats: List[Beat] = Field(default_factory=list)


class ClipSpec(BaseModel):
    """Specification for generating a video clip."""
    grok_prompt: str
    beat_id: str
    duration_sec: float


class VideoResult(BaseModel):
    """Result of video assembly."""
    output_path: Path
    duration_sec: float
    clip_paths: List[Path] = Field(default_factory=list)