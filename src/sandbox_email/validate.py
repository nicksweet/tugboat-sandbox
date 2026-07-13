"""Email validation utilities for sandbox_email package."""


def is_valid_email(text: str) -> bool:
    """
    Validate email syntax.

    Returns True only when the string contains exactly one '@' with non-empty
    local and domain parts, and the domain part contains at least one '.'.

    Examples:
        "user@example.com" -> True
        "bad" -> False
        "@" -> False
        "a@b" -> False
        "a@b." -> False
    """
    if not isinstance(text, str):
        return False

    # Check for exactly one '@'
    if text.count('@') != 1:
        return False

    local, domain = text.split('@', 1)

    # Both local and domain parts must be non-empty
    if not local or not domain:
        return False

    # Domain must contain at least one '.'
    if '.' not in domain:
        return False

    # Domain must not end with '.'
    if domain.endswith('.'):
        return False

    return True