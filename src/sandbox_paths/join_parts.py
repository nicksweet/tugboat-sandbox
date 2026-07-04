def join_parts(*parts: str) -> str:
    """Join non-empty path components with '/', skipping empty strings."""
    return '/'.join(part for part in parts if part)