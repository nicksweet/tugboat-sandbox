def dedupe_sorted(nums: list[int]) -> list[int]:
    """Return a sorted list of unique integers from the input."""
    return sorted(set(nums))