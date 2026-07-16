from dataclasses import dataclass
from typing import List, Optional


@dataclass
class EventInput:
    title: str
    doc_paths: Optional[List[str]] = None


@dataclass
class Beat:
    order: int
    slug: str
    action: str
    duration_sec: float


@dataclass
class Screenplay:
    title: str
    beats: List[Beat]
    target_duration_sec: float = 150.0