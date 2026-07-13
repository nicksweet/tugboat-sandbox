import re


def normalize_digits(text: str) -> str:
    """Return only digit characters from the input string."""
    return re.sub(r'\D', '', text)