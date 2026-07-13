"""Domain models for history video generation."""

from pydantic import BaseModel, Field
from typing import List, Optional


class Beat(BaseModel):
    """A single beat in a screenplay."""

    order: int
    slug: str
    action: str
    duration_sec: float


class Screenplay(BaseModel):
    """A complete screenplay with beats."""

    title: str
    target_duration_sec: float
    beats: List[Beat]


class ClipDescription(BaseModel):
    """Description of a video clip to generate."""

    id: str
    description: str
    duration_seconds: float
    visual_prompt: str
    audio_prompt: str
    start_time: float
    end_time: float


class ClipManifestEntry(BaseModel):
    """A single clip entry in an assembly manifest."""

    path: str
    duration: float


class AssemblyManifest(BaseModel):
    """Manifest for assembling final video from clips."""

    clips: List[ClipManifestEntry]
    total_duration: float
    output_path: str