def parse_hms(text: str) -> int:
    """Parse a HH:MM:SS string into total seconds.
    
    Args:
        text: A string in the format HH:MM:SS where each component is two digits.
        
    Returns:
        Total seconds as an integer.
        
    Raises:
        ValueError: If the input does not match the exact HH:MM:SS format,
                    contains non-digits, or components are out of range.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    parts = text.split(':')
    if len(parts) != 3:
        raise ValueError(f"Expected exactly three components separated by ':', got {len(parts)}")
    
    for part in parts:
        if len(part) != 2 or not part.isdigit():
            raise ValueError(f"Each component must be two digits, got '{part}'")
    
    try:
        hours, minutes, seconds = (int(part) for part in parts)
    except ValueError:
        # This should not happen because we checked isdigit, but just in case.
        raise ValueError("Components must be integers")
    
    if not (0 <= hours <= 99):
        raise ValueError(f"Hours must be between 0 and 99, got {hours}")
    if not (0 <= minutes <= 59):
        raise ValueError(f"Minutes must be between 0 and 59, got {minutes}")
    if not (0 <= seconds <= 59):
        raise ValueError(f"Seconds must be between 0 and 59, got {seconds}")
    
    return hours * 3600 + minutes * 60 + seconds