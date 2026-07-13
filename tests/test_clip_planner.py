"""Unit tests for clip_planner module."""

import os

os.environ["HISTVIDEO_OFFLINE"] = "1"

import pytest
from history_video.clip_planner import plan_clips, load_screenplay_offline
from history_video.models import ClipDescription
from history_video.screenplay import load_screenplay


def test_plan_clips_returns_list():
    """Test that plan_clips returns a list of ClipDescription objects."""
    screenplay = load_screenplay("tests/fixtures/history_video/screenplay.json")
    clips = plan_clips(screenplay)

    assert isinstance(clips, list), "Expected list of clips"
    assert len(clips) > 0, "Expected at least one clip"


def test_plan_clips_count_in_range():
    """Test that plan_clips produces 12-18 clips."""
    screenplay = load_screenplay("tests/fixtures/history_video/screenplay.json")
    clips = plan_clips(screenplay)

    assert 12 <= len(clips) <= 18, f"Expected 12-18 clips, got {len(clips)}"


def test_plan_clips_structure():
    """Test that each clip has correct ClipDescription structure."""
    screenplay = load_screenplay("tests/fixtures/history_video/screenplay.json")
    clips = plan_clips(screenplay)

    for clip in clips:
        assert isinstance(clip, ClipDescription), f"Not ClipDescription: {type(clip)}"
        assert clip.id != "", "Empty clip id"
        assert clip.duration_seconds > 0, "Invalid duration"
        assert clip.description != "", "Empty description"
        assert clip.visual_prompt != "", "Empty visual_prompt"
        assert clip.audio_prompt != "", "Empty audio_prompt"
        assert clip.start_time >= 0, "Negative start_time"
        assert clip.end_time > clip.start_time, "end_time not after start_time"


def test_plan_clips_sequential_timing():
    """Test that clips have sequential, non-overlapping timing."""
    screenplay = load_screenplay("tests/fixtures/history_video/screenplay.json")
    clips = plan_clips(screenplay)

    for i in range(len(clips) - 1):
        assert clips[i].end_time == clips[i + 1].start_time, \
            f"Clip {i} end_time ({clips[i].end_time}) != Clip {i+1} start_time ({clips[i+1].start_time})"


def test_plan_clips_total_duration():
    """Test that total clip duration matches screenplay target."""
    screenplay = load_screenplay("tests/fixtures/history_video/screenplay.json")
    clips = plan_clips(screenplay)

    total_duration = sum(clip.duration_seconds for clip in clips)
    assert abs(total_duration - screenplay.target_duration_sec) < 0.01, \
        f"Total duration {total_duration} != target {screenplay.target_duration_sec}"


def test_load_screenplay_offline():
    """Test offline screenplay loading."""
    screenplay = load_screenplay_offline()

    assert screenplay.title == "Moon Landing 1969"
    assert screenplay.target_duration_sec == 150.0
    assert len(screenplay.beats) == 3


def test_clip_ids_sequential():
    """Test that clip IDs are sequential starting from clip_001."""
    screenplay = load_screenplay("tests/fixtures/history_video/screenplay.json")
    clips = plan_clips(screenplay)

    for i, clip in enumerate(clips):
        expected_id = f"clip_{i + 1:03d}"
        assert clip.id == expected_id, f"Expected {expected_id}, got {clip.id}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])