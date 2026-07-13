"""Clip planner: maps Screenplay beats to ClipSpec objects."""

from history_video.models import Beat, ClipSpec, Screenplay


def plan_clips(screenplay: Screenplay) -> list[ClipSpec]:
    """Convert a Screenplay into a list of ClipSpec objects, one per beat.

    Each ClipSpec is derived from its corresponding Beat:
    - grok_prompt combines narration and visual_description
    - beat_id is the beat's id
    - duration_sec is the beat's duration_sec
    """
    clips: list[ClipSpec] = []
    for beat in screenplay.beats:
        grok_prompt = f"{beat.narration}. Visual: {beat.visual_description}"
        clip = ClipSpec(
            grok_prompt=grok_prompt,
            beat_id=beat.id,
            duration_sec=beat.duration_sec,
        )
        clips.append(clip)
    return clips