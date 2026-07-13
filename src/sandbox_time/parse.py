"""Parse HH:MM:SS time strings into total seconds."""


def parse_hms(text: str) -> int:
    """
    Parse a zero-padded HH:MM:SS string into total seconds.

    Args:
        text: Time string in format "HH:MM:SS" where:
            - HH is 00-23 (hours)
            - MM is 00-59 (minutes)
            - SS is 00-59 (seconds)

    Returns:
        Total seconds as an integer.

    Raises:
        ValueError: If the format is invalid or values are out of range.
    """
    if not isinstance(text, str):
        raise ValueError(f"Expected string, got {type(text).__name__}")

    parts = text.split(":")
    if len(parts) != 3:
        raise ValueError(f"Invalid format: expected HH:MM:SS, got {text!r}")

    try:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
    except ValueError:
        raise ValueError(f"Non-numeric components in {text!r}")

    # Validate zero-padding (each component must be exactly 2 digits)
    if len(parts[0]) != 2 or len(parts[1]) != 2 or len(parts[2]) != 2:
        raise ValueError(f"Components must be zero-padded to 2 digits: {text!r}")

    # Validate ranges
    if not (0 <= hours <= 23):
        raise ValueError(f"Hours must be 00-23, got {hours:02d}")
    if not (0 <= minutes <= 59):
        raise ValueError(f"Minutes must be 00-59, got {minutes:02d}")
    if not (0 <= seconds <= 59):
        raise ValueError(f"Seconds must be 00-59, got {seconds:02d}")

    return hours * 3600 + minutes * 60 + seconds