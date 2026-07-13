def normalize_digits(text: str) -> str:
    """Return a string containing only the digit characters from the input, preserving their order."""
    return ''.join(ch for ch in text if ch.isdigit())