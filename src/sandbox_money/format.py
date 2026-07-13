def cents_to_str(cents: int) -> str:
    """Format integer cents as USD string with two decimal places and leading dollar sign."""
    dollars = cents // 100
    remaining_cents = abs(cents) % 100
    sign = "-" if cents < 0 else ""
    return f"{sign}${dollars}.{remaining_cents:02d}"