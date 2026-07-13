"""Phone number formatting utilities."""


def format_us(digits: str) -> str:
    """Format a 10-digit string as (XXX) XXX-XXXX.

    Args:
        digits: A string of exactly 10 digits.

    Returns:
        The formatted phone number string.
    """
    if len(digits) != 10 or not digits.isdigit():
        raise ValueError("Expected exactly 10 digits")
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"