def join_parts(*parts: str) -> str:
    """Join non-empty string parts with '/' separator.

    Args:
        *parts: Variable number of string parts to join.

    Returns:
        A string with non-empty parts joined by '/'.

    Examples:
        >>> join_parts("a", "b", "c")
        'a/b/c'
        >>> join_parts("a", "", "c")
        'a/c'
    """
    return "/".join(part for part in parts if part)