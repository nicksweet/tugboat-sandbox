"""Time formatting utilities for sandbox_time package."""


def format_seconds(total: int) -> str:
    """Format non-negative seconds as zero-padded HH:MM:SS.

    Args:
        total: Non-negative integer representing total seconds.

    Returns:
        String in HH:MM:SS format with zero-padded components.

    Examples:
        >>> format_seconds(3661)
        '01:01:01'
        >>> format_seconds(0)
        '00:00:00'
    """
    if total < 0:
        raise ValueError("total must be non-negative")

    hours = total // 3600
    minutes = (total % 3600) // 60
    seconds = total % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"