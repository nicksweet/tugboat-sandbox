def cents_to_str(cents: int) -> str:
    """Format integer cents as USD string with two decimal places and leading dollar sign.

    Args:
        cents: Amount in cents (can be negative or positive).

    Returns:
        Formatted string like '$12.34' for 1234 cents or '-$12.34' for -1234 cents.
    """
    sign = '-' if cents < 0 else ''
    cents_abs = abs(cents)
    dollars = cents_abs // 100
    cents_part = cents_abs % 100
    return f"{sign}${dollars}.{cents_part:02d}"