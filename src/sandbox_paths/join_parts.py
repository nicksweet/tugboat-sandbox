def join_parts(*parts: str) -> str:
    """Join non-empty parts with '/' separator, skipping empty parts."""
    return "/".join(part for part in parts if part)