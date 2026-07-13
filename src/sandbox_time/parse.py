def parse_hms(text: str) -> int:
    """
    Parse HH:MM:SS string into total seconds.
    Raises ValueError on invalid format, negative, non-numeric, out-of-range values.
    """
    if not text or text != text.strip():
        raise ValueError("Invalid format")
    parts = text.split(":")
    if len(parts) != 3:
        raise ValueError("Invalid format")
    try:
        h, m, s = map(int, parts)
    except ValueError:
        raise ValueError("Non-numeric component")
    if h < 0 or m < 0 or s < 0:
        raise ValueError("Negative value")
    if h >= 24 or m >= 60 or s >= 60:
        raise ValueError("Out-of-range")
    return h * 3600 + m * 60 + s