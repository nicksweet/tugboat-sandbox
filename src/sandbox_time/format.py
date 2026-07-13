def format_seconds(total: int) -> str:
    """Format non-negative seconds as zero-padded HH:MM:SS string."""
    if total < 0:
        raise ValueError("total must be non-negative")
    hours = total // 3600
    minutes = (total % 3600) // 60
    seconds = total % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"