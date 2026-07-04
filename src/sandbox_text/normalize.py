def normalize_ws(s: str) -> str:
    """Strip leading/trailing whitespace and collapse internal whitespace runs to a single space."""
    return ' '.join(s.split())