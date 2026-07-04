def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    """Merge two sorted ascending integer lists into a single sorted list."""
    i, j = 0, 0
    merged: list[int] = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    # Append remaining elements
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged