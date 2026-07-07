def slug(s: str) -> str:
    """Convert a string to a URL-friendly slug.
    Lowercases the input, replaces consecutive whitespace with a single hyphen,
    and returns an empty string for empty input.
    """
    if not s:
        return ""
    # Lowercase and split on whitespace (any amount) then join with hyphen
    return "-".join(s.lower().split())