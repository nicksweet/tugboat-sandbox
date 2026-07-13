"""Clip planner module for breaking a Screenplay into ClipDescription objects."""

import os
from typing import List

from history_video.models import ClipDescription, Screenplay


def plan_clips(screenplay: Screenplay) -> List[ClipDescription]:
    """
    Divide a screenplay into 12-18 ClipDescription objects.

    Args:
        screenplay: The Screenplay to divide into clips.

    Returns:
        List of ClipDescription objects (12-18 clips).
    """
    clips = []
    current_time = 0.0
    clip_counter = 1

    # Calculate clips per beat to get 12-18 total clips
    num_beats = len(screenplay.beats)
    # Target 15 clips (middle of 12-18 range)
    target_clips = 15
    clips_per_beat = max(1, target_clips // num_beats)

    for beat in screenplay.beats:
        beat_duration = beat.duration_sec
        # Distribute clips across beats
        num_clips_for_beat = clips_per_beat
        # Adjust for last beat to hit target
        if beat.order == num_beats:
            remaining_clips = target_clips - len(clips)
            num_clips_for_beat = max(1, remaining_clips)

        clip_duration = beat_duration / num_clips_for_beat

        for i in range(num_clips_for_beat):
            start_time = current_time + (i * clip_duration)
            end_time = start_time + clip_duration

            clip = ClipDescription(
                id=f"clip_{clip_counter:03d}",
                description=f"{beat.slug} - part {i + 1}",
                duration_seconds=clip_duration,
                visual_prompt=beat.action,
                audio_prompt=f"Narration for {beat.slug} part {i + 1}",
                start_time=start_time,
                end_time=end_time,
            )
            clips.append(clip)
            clip_counter += 1

        current_time += beat_duration

    # Ensure we have 12-18 clips
    if len(clips) < 12:
        # Add more clips by subdividing the longest beats
        while len(clips) < 12:
            # Find the clip with longest duration to split
            longest_idx = max(range(len(clips)), key=lambda i: clips[i].duration_seconds)
            longest_clip = clips[longest_idx]
            half_duration = longest_clip.duration_seconds / 2

            # Replace with two clips
            new_clip_1 = ClipDescription(
                id=f"clip_{clip_counter:03d}",
                description=f"{longest_clip.description} (part 1)",
                duration_seconds=half_duration,
                visual_prompt=longest_clip.visual_prompt,
                audio_prompt=longest_clip.audio_prompt,
                start_time=longest_clip.start_time,
                end_time=longest_clip.start_time + half_duration,
            )
            new_clip_2 = ClipDescription(
                id=f"clip_{clip_counter + 1:03d}",
                description=f"{longest_clip.description} (part 2)",
                duration_seconds=half_duration,
                visual_prompt=longest_clip.visual_prompt,
                audio_prompt=longest_clip.audio_prompt,
                start_time=longest_clip.start_time + half_duration,
                end_time=longest_clip.end_time,
            )
            clips[longest_idx] = new_clip_1
            clips.insert(longest_idx + 1, new_clip_2)
            clip_counter += 2

    elif len(clips) > 18:
        # Merge clips if too many
        while len(clips) > 18:
            # Merge the two shortest adjacent clips
            min_duration = float('inf')
            merge_idx = 0
            for i in range(len(clips) - 1):
                combined = clips[i].duration_seconds + clips[i + 1].duration_seconds
                if combined < min_duration:
                    min_duration = combined
                    merge_idx = i

            merged = ClipDescription(
                id=f"clip_{clip_counter:03d}",
                description=f"{clips[merge_idx].description} + {clips[merge_idx + 1].description}",
                duration_seconds=clips[merge_idx].duration_seconds + clips[merge_idx + 1].duration_seconds,
                visual_prompt=clips[merge_idx].visual_prompt,
                audio_prompt=clips[merge_idx].audio_prompt,
                start_time=clips[merge_idx].start_time,
                end_time=clips[merge_idx + 1].end_time,
            )
            clips[merge_idx] = merged
            clips.pop(merge_idx + 1)
            clip_counter += 1

    # Renumber clip IDs sequentially
    for i, clip in enumerate(clips):
        clip.id = f"clip_{i + 1:03d}"

    return clips


def load_screenplay_offline() -> Screenplay:
    """
    Load the screenplay fixture in offline mode.

    Returns:
        Screenplay loaded from tests/fixtures/history_video/screenplay.json
    """
    from history_video.screenplay import load_screenplay
    return load_screenplay("tests/fixtures/history_video/screenplay.json")