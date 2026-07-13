def cents_to_str(cents: int) -> str:
    """Format integer cents as USD string with leading dollar sign and two decimal places.

    Args:
        cents: Amount in cents (e.g., 1234 for $12.34)

    Returns:
        Formatted USD string (e.g., "$12.34")
    """
    dollars = cents // 100
    remaining_cents = cents % 100
    return f"${dollars}.{remaining_cents:02d}"