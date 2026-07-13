"""Merge utilities for sorted lists."""


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    """Merge two pre-sorted ascending integer lists into one sorted list.

    Uses a two-pointer merge algorithm (O(n+m)) since inputs are already sorted.

    Args:
        a: First sorted list of integers.
        b: Second sorted list of integers.

    Returns:
        A new list containing all elements from both inputs in sorted order.

    Example:
        >>> merge_sorted([1, 3], [2, 4])
        [1, 2, 3, 4]
    """
    result = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # Append remaining elements
    result.extend(a[i:])
    result.extend(b[j:])

    return result