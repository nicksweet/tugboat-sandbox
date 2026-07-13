"""Parse USD-formatted strings into integer cents."""


def parse_cents(text: str) -> int:
    """Parse a USD-formatted string into integer cents.

    Args:
        text: A string like "$12.34" or "12.34"

    Returns:
        Integer cents (e.g., 1234 for "$12.34")

    Raises:
        ValueError: If the input cannot be parsed as a valid USD amount.
    """
    # Remove whitespace and optional dollar sign
    cleaned = text.strip().lstrip("$")

    # Handle negative amounts
    is_negative = cleaned.startswith("-")
    if is_negative:
        cleaned = cleaned[1:]

    # Split into dollars and cents
    if "." in cleaned:
        dollars_str, cents_str = cleaned.split(".", 1)
        # Pad or truncate cents to exactly 2 digits
        if len(cents_str) == 1:
            cents_str = cents_str + "0"
        elif len(cents_str) > 2:
            cents_str = cents_str[:2]
    else:
        dollars_str = cleaned
        cents_str = "00"

    # Validate that dollars and cents are numeric
    if not dollars_str.isdigit():
        raise ValueError(f"Invalid dollar amount: {text}")
    if not cents_str.isdigit():
        raise ValueError(f"Invalid cents amount: {text}")

    dollars = int(dollars_str)
    cents = int(cents_str)

    total_cents = dollars * 100 + cents
    return -total_cents if is_negative else total_cents