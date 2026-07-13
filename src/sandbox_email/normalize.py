"""Email normalization utilities."""


def normalize_email(text: str) -> str:
    """Normalize an email address by stripping whitespace and lowercasing.

    Args:
        text: The email address string to normalize.

    Returns:
        The normalized email address (lowercase, no leading/trailing whitespace).

    Example:
        >>> normalize_email("  User@Example.COM  ")
        'user@example.com'
    """
    return text.strip().lower()