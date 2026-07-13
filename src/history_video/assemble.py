"""Assembly module for concatenating video clips using ffmpeg."""

import subprocess
from pathlib import Path


def assemble_clips(clip_paths: list[Path], output_path: Path) -> None:
    """
    Concatenate video clips into a single MP4 using ffmpeg concat demuxer.

    Args:
        clip_paths: List of paths to input video clips (must be same codec/format)
        output_path: Path where the concatenated output MP4 will be written
    """
    if not clip_paths:
        raise ValueError("No clip paths provided")

    # Create a temporary concat file listing all clips
    concat_file = output_path.with_suffix(".txt")
    try:
        with concat_file.open("w") as f:
            for clip in clip_paths:
                # Use absolute paths for safety
                f.write(f"file '{clip.resolve()}'\n")

        # Run ffmpeg concat
        cmd = [
            "ffmpeg",
            "-y",  # Overwrite output
            "-f", "concat",
            "-safe", "0",
            "-i", str(concat_file),
            "-c", "copy",  # Stream copy (no re-encode)
            str(output_path),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"ffmpeg concat failed: {result.stderr}")
    finally:
        # Clean up concat file
        if concat_file.exists():
            concat_file.unlink()