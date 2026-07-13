"""Parse USD-formatted strings to integer cents."""


def parse_cents(text: str) -> int:
    """Parse a USD-formatted string to integer cents.

    Args:
        text: A string like "$12.34" representing dollars and cents.

    Returns:
        The amount in cents as an integer (e.g., 1234 for "$12.34").
    """
    # Remove the dollar sign and any whitespace
    cleaned = text.strip().lstrip("$")
    # Split on decimal point
    if "." in cleaned:
        dollars, cents = cleaned.split(".")
        # Pad cents to 2 digits if needed
        cents = cents.ljust(2, "0")[:2]
    else:
        dollars = cleaned
        cents = "00"
    return int(dollars) * 100 + int(cents)