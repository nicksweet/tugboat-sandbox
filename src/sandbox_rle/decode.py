"""Run-length decoding for letter-only RLE strings."""

import re


def decode(text: str) -> str:
    """
    Decode a run-length encoded string produced by encode().

    Parses <letter><digits> sequences and expands them.
    Non-letter characters pass through unchanged.

    Args:
        text: RLE-encoded string (e.g., "a3b2c1")

    Returns:
        Decoded string (e.g., "aaabbc")
    """
    if not text:
        return ""

    result = []
    i = 0
    while i < len(text):
        char = text[i]
        if char.isalpha():
            # Parse the count digits following the letter
            i += 1
            count_str = ""
            while i < len(text) and text[i].isdigit():
                count_str += text[i]
                i += 1
            count = int(count_str) if count_str else 1
            result.append(char * count)
        else:
            # Non-letter characters pass through unchanged
            result.append(char)
            i += 1

    return "".join(result)