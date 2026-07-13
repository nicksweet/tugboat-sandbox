"""Unit tests for domain models."""

import json
from pathlib import Path
import sys

sys.path.insert(0, "src")

from history_video.models import (
    Beat,
    Screenplay,
    ClipDescription,
    ClipManifestEntry,
    AssemblyManifest,
)


def test_screenplay_from_fixture():
    """Test Screenplay model instantiation from fixture data."""
    fixture_path = Path("tests/fixtures/history_video/screenplay.json")
    with open(fixture_path) as f:
        data = json.load(f)

    screenplay = Screenplay(**data)

    assert screenplay.title == "Moon Landing 1969"
    assert screenplay.target_duration_sec == 150.0
    assert len(screenplay.beats) == 3

    beat1 = screenplay.beats[0]
    assert beat1.order == 1
    assert beat1.slug == "launch-pad"
    assert "Saturn V" in beat1.action
    assert beat1.duration_sec == 50.0


def test_clip_description():
    """Test ClipDescription model instantiation."""
    clip = ClipDescription(
        id="clip_1",
        description="Test clip",
        duration_seconds=5.0,
        visual_prompt="A test scene",
        audio_prompt="Narration here",
        start_time=0.0,
        end_time=5.0,
    )

    assert clip.id == "clip_1"
    assert clip.description == "Test clip"
    assert clip.duration_seconds == 5.0
    assert clip.visual_prompt == "A test scene"
    assert clip.audio_prompt == "Narration here"
    assert clip.start_time == 0.0
    assert clip.end_time == 5.0


def test_assembly_manifest():
    """Test AssemblyManifest model instantiation."""
    manifest = AssemblyManifest(
        clips=[
            ClipManifestEntry(path="tests/fixtures/history_video/clips/beat01.mp4", duration=5.0),
            ClipManifestEntry(path="tests/fixtures/history_video/clips/beat02.mp4", duration=5.0),
            ClipManifestEntry(path="tests/fixtures/history_video/clips/beat03.mp4", duration=5.0),
        ],
        total_duration=15.0,
        output_path="output.mp4",
    )

    assert manifest.total_duration == 15.0
    assert len(manifest.clips) == 3
    assert manifest.output_path == "output.mp4"
    assert manifest.clips[0].path == "tests/fixtures/history_video/clips/beat01.mp4"
    assert manifest.clips[0].duration == 5.0


def test_beat_model():
    """Test Beat model instantiation."""
    beat = Beat(
        order=1,
        slug="test-beat",
        action="Test action",
        duration_sec=10.0,
    )

    assert beat.order == 1
    assert beat.slug == "test-beat"
    assert beat.action == "Test action"
    assert beat.duration_sec == 10.0


def test_clip_manifest_entry():
    """Test ClipManifestEntry model instantiation."""
    entry = ClipManifestEntry(
        path="tests/fixtures/history_video/clips/beat01.mp4",
        duration=5.0,
    )

    assert entry.path == "tests/fixtures/history_video/clips/beat01.mp4"
    assert entry.duration == 5.0


if __name__ == "__main__":
    test_screenplay_from_fixture()
    test_clip_description()
    test_assembly_manifest()
    test_beat_model()
    test_clip_manifest_entry()
    print("All tests passed!")