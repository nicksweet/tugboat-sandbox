"""Letters-only run-length decoding."""

import re


def decode(text: str) -> str:
    """
    Decode text encoded with letters-only run-length encoding.

    Reverses the output of encode: each <char><count> pattern becomes
    the character repeated count times. Non-letter characters pass through unchanged.

    Args:
        text: Encoded string to decode.

    Returns:
        Decoded string with letter runs expanded.
    """
    if not text:
        return ""

    result = []
    i = 0
    n = len(text)

    while i < n:
        char = text[i]
        if char.isalpha():
            # Parse the count (digits following the letter)
            j = i + 1
            count_str = ""
            while j < n and text[j].isdigit():
                count_str += text[j]
                j += 1

            if count_str:
                count = int(count_str)
                result.append(char * count)
            else:
                # Single letter without count (shouldn't happen with valid encode output)
                result.append(char)
            i = j
        else:
            # Non-letter passes through unchanged
            result.append(char)
            i += 1

    return "".join(result)