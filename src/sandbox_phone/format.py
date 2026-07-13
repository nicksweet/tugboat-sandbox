def format_us(digits: str) -> str:
    """Format a 10-digit US phone number as (XXX) XXX-XXXX."""
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"