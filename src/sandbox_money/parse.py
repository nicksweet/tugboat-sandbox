def parse_cents(text: str) -> int:
    """Parse a USD-formatted string with '$' prefix and two decimal places into integer cents.
    
    Args:
        text: A string like "$12.34"
        
    Returns:
        Integer cents, e.g., 1234 for "$12.34"
    """
    # Remove the leading '$'
    if not text.startswith('$'):
        raise ValueError("Input must start with '$'")
    amount = text[1:]
    # Split dollars and cents
    if '.' not in amount:
        raise ValueError("Input must contain a decimal point")
    dollars, cents = amount.split('.')
    # Ensure cents has exactly two digits
    if len(cents) != 2:
        raise ValueError("Cents must have exactly two decimal places")
    # Convert to integer cents
    return int(dollars) * 100 + int(cents)