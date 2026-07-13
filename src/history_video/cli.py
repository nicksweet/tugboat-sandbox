"""CLI entry point for history video generation."""

import os
from pathlib import Path
from typing import Optional

import typer
from typer.testing import CliRunner

from history_video.models import Screenplay, ClipDescription
from history_video.research import generate_screenplay
from history_video.clip_planner import plan_clips
from history_video.clip_generator import generate_clips
from history_video.assemble import assemble_clips

app = typer.Typer(
    name="history-video",
    help="Generate historical documentary videos from event titles.",
    no_args_is_help=True,
)


@app.command()
def generate(
    event_title: str = typer.Argument(..., help="Title of the historical event"),
    genre: str = typer.Option("documentary", "--genre", "-g", help="Video genre"),
    role: str = typer.Option("narrator", "--role", "-r", help="Narrator role"),
    out: Path = typer.Option(..., "--out", "-o", help="Output MP4 file path"),
) -> None:
    """Generate a history video for the given event title."""
    # Force offline mode for CLI
    os.environ["HISTVIDEO_OFFLINE"] = "1"

    typer.echo(f"Generating video for: {event_title}")
    typer.echo(f"Genre: {genre}, Role: {role}")
    typer.echo(f"Output: {out}")

    # Step 1: Generate screenplay
    typer.echo("Step 1/4: Generating screenplay...")
    screenplay: Screenplay = generate_screenplay(event_title)
    typer.echo(f"  Screenplay: {screenplay.title} ({screenplay.target_duration_sec:.1f}s, {len(screenplay.beats)} beats)")

    # Step 2: Plan clips
    typer.echo("Step 2/4: Planning clips...")
    clip_descriptions: list[ClipDescription] = plan_clips(screenplay)
    typer.echo(f"  Planned {len(clip_descriptions)} clips")

    # Step 3: Generate clips
    typer.echo("Step 3/4: Generating clips...")
    clip_paths = generate_clips(clip_descriptions)
    typer.echo(f"  Generated {len(clip_paths)} clip files")

    # Step 4: Assemble final video
    typer.echo("Step 4/4: Assembling final video...")
    assemble_clips(clip_paths, out)
    typer.echo(f"  Video assembled: {out}")

    typer.echo("Done!")


if __name__ == "__main__":
    app()