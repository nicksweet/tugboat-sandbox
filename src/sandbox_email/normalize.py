"""Email normalization utilities."""


def normalize_email(text: str) -> str:
    """Normalize an email address by stripping whitespace and lowercasing.

    Args:
        text: The email address string to normalize.

    Returns:
        The normalized email address (lowercase, no leading/trailing whitespace).
    """
    return text.strip().lower()