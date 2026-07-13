"""CLI entry point for history_video pipeline."""

import os
from pathlib import Path
from typing import List, Optional

import typer

from history_video.models import InputRequest
from history_video.research import gather_context
from history_video.screenplay import generate_screenplay
from history_video.clip_planner import plan_clips
from history_video.clip_generator import generate_clips
from history_video.assembler import assemble_video


app = typer.Typer(
    name="history-video",
    help="Generate historical event videos from text descriptions.",
    add_completion=False,
)


@app.command()
def history_video(
    event_title: str = typer.Argument(..., help="Title of the historical event"),
    genre: str = typer.Option("documentary", "--genre", "-g", help="Genre/style of the video"),
    role: str = typer.Option("narrator", "--role", "-r", help="Narrative role/perspective"),
    supporting_doc: List[Path] = typer.Option(
        [], "--supporting-doc", "-s", help="Path to supporting document (repeatable)"
    ),
    offline: bool = typer.Option(
        False, "--offline", help="Run in offline mode using seeded fixtures"
    ),
    output: Path = typer.Option(
        Path("output.mp4"), "--output", "-o", help="Output MP4 file path"
    ),
) -> None:
    """
    Generate a historical event video from a title and optional parameters.

    This command orchestrates the full pipeline:
    1. Research - gather context for the event
    2. Screenplay - generate beat-sheet guided screenplay
    3. Clip Planning - map beats to clip specifications
    4. Clip Generation - produce video clips (offline uses seeded fixtures)
    5. Assembly - stitch clips into final MP4 using ffmpeg
    """
    # Set offline mode environment variable if requested
    if offline:
        os.environ["HISTVIDEO_OFFLINE"] = "1"

    # Build input request
    request = InputRequest(
        event_title=event_title,
        genre=genre,
        role=role,
        supporting_docs=supporting_doc,
    )

    typer.echo(f"Generating video for: {event_title}")
    typer.echo(f"Genre: {genre}, Role: {role}")
    if supporting_doc:
        typer.echo(f"Supporting docs: {len(supporting_doc)} file(s)")
    typer.echo(f"Offline mode: {offline}")
    typer.echo(f"Output: {output}")

    # Stage 1: Research - gather context
    typer.echo("\n[1/5] Gathering context...")
    context = gather_context(request)
    typer.echo(f"  Event: {context.get('event_title', 'N/A')}")

    # Stage 2: Screenplay generation
    typer.echo("\n[2/5] Generating screenplay...")
    screenplay = generate_screenplay(context, request)
    typer.echo(f"  Beats: {len(screenplay.beats)}")
    for beat in screenplay.beats:
        typer.echo(f"    - {beat.id}: {beat.duration_sec}s")

    # Stage 3: Clip planning
    typer.echo("\n[3/5] Planning clips...")
    clip_specs = plan_clips(screenplay)
    typer.echo(f"  Clip specs: {len(clip_specs)}")

    # Stage 4: Clip generation
    typer.echo("\n[4/5] Generating clips...")
    clip_paths = generate_clips(clip_specs)
    typer.echo(f"  Clips: {len(clip_paths)}")
    for path in clip_paths:
        typer.echo(f"    - {path}")

    # Stage 5: Video assembly
    typer.echo("\n[5/5] Assembling video...")
    result = assemble_video(clip_paths, output)
    typer.echo(f"  Output: {result.output_path}")
    typer.echo(f"  Duration: {result.duration_sec:.2f}s")

    typer.echo("\n✓ Video generation complete!")


if __name__ == "__main__":
    app()