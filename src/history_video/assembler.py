"""Video assembler module for stitching clips using ffmpeg concat."""

import subprocess
import tempfile
from pathlib import Path
from typing import List

from history_video.models import VideoResult


def _run_ffmpeg_concat(clip_paths: List[Path], output_path: Path) -> None:
    """Run ffmpeg concat to stitch clips into a single video."""
    # Create a temporary concat list file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        for clip_path in clip_paths:
            # Use absolute paths for safety
            f.write(f"file '{clip_path.absolute()}'\n")
        concat_list_path = Path(f.name)

    try:
        # Run ffmpeg concat
        cmd = [
            'ffmpeg',
            '-f', 'concat',
            '-safe', '0',
            '-i', str(concat_list_path),
            '-c', 'copy',
            '-y',  # Overwrite output file if exists
            str(output_path)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"ffmpeg concat failed: {result.stderr}")
    finally:
        # Clean up the temporary concat list file
        concat_list_path.unlink(missing_ok=True)


def _get_video_duration(video_path: Path) -> float:
    """Get video duration in seconds using ffprobe."""
    cmd = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        str(video_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"ffprobe failed: {result.stderr}")
    try:
        duration = float(result.stdout.strip())
        return duration
    except ValueError:
        raise RuntimeError(f"Could not parse duration from ffprobe output: {result.stdout}")


def assemble_video(clip_paths: List[Path], output_path: Path) -> VideoResult:
    """
    Stitch a list of clip file paths into a single MP4 using ffmpeg concat.
    
    Args:
        clip_paths: List of paths to video clips to concatenate
        output_path: Path where the assembled video will be written
        
    Returns:
        VideoResult with output_path, duration_sec, and clip_paths
        
    Raises:
        RuntimeError: If ffmpeg or ffprobe fails, or duration is not positive
    """
    if not clip_paths:
        raise ValueError("clip_paths cannot be empty")
    
    # Verify all input clips exist
    for clip_path in clip_paths:
        if not clip_path.exists():
            raise FileNotFoundError(f"Clip not found: {clip_path}")
    
    # Run ffmpeg concat
    _run_ffmpeg_concat(clip_paths, output_path)
    
    # Verify output exists
    if not output_path.exists():
        raise RuntimeError(f"Output file was not created: {output_path}")
    
    # Get duration via ffprobe
    duration_sec = _get_video_duration(output_path)
    
    if duration_sec <= 0:
        raise RuntimeError(f"Assembled video has non-positive duration: {duration_sec}")
    
    return VideoResult(
        output_path=output_path,
        duration_sec=duration_sec,
        clip_paths=clip_paths
    )