def parse_hms(text: str) -> int:
    """Parse a HH:MM:SS string into total seconds.

    Args:
        text: A string in the format HH:MM:SS.

    Returns:
        Total seconds as an integer.

    Raises:
        ValueError: If the input does not match HH:MM:SS, contains non-digits,
                    or has out-of-range values (hours not in 0-23, minutes/seconds not in 0-59).
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    parts = text.split(':')
    if len(parts) != 3:
        raise ValueError(f"Invalid format: expected HH:MM:SS, got '{text}'")

    for part in parts:
        if len(part) != 2 or not part.isdigit():
            raise ValueError(f"Each part must be two digits, got '{part}' in '{text}'")

    try:
        hours, minutes, seconds = (int(part) for part in parts)
    except ValueError:
        # This should not happen because we checked isdigit, but keep for safety.
        raise ValueError(f"Non-digit value in '{text}'")

    if not (0 <= hours <= 23):
        raise ValueError(f"Hours out of range (0-23): {hours}")
    if not (0 <= minutes <= 59):
        raise ValueError(f"Minutes out of range (0-59): {minutes}")
    if not (0 <= seconds <= 59):
        raise ValueError(f"Seconds out of range (0-59): {seconds}")

    return hours * 3600 + minutes * 60 + seconds