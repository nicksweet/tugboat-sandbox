"""Letters-only run-length encoding."""

import re


def encode(text: str) -> str:
    """
    Encode text using letters-only run-length encoding.

    Each maximal run of the same letter becomes <char><count>.
    Non-letter characters pass through unchanged.

    Args:
        text: Input string to encode.

    Returns:
        Encoded string with letter runs compressed.
    """
    if not text:
        return ""

    result = []
    i = 0
    n = len(text)

    while i < n:
        char = text[i]
        if char.isalpha():
            # Count consecutive same letters
            count = 1
            j = i + 1
            while j < n and text[j] == char:
                count += 1
                j += 1
            result.append(f"{char}{count}")
            i = j
        else:
            # Non-letter passes through unchanged
            result.append(char)
            i += 1

    return "".join(result)