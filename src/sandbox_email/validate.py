"""Email validation utilities for sandbox_email package."""


def is_valid_email(text: str) -> bool:
    """
    Validate an email address syntactically.

    Returns True iff the string contains exactly one '@', both local and domain
    parts are non-empty, and the domain part contains at least one '.'.

    Examples:
        >>> is_valid_email("user@example.com")
        True
        >>> is_valid_email("bad")
        False
        >>> is_valid_email("user@")
        False
        >>> is_valid_email("@example.com")
        False
        >>> is_valid_email("user@example")
        False
    """
    if not isinstance(text, str):
        return False

    # Check for exactly one '@'
    if text.count('@') != 1:
        return False

    local_part, domain_part = text.split('@', 1)

    # Both parts must be non-empty
    if not local_part or not domain_part:
        return False

    # Domain must contain at least one '.'
    if '.' not in domain_part:
        return False

    return True