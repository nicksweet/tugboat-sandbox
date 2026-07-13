def encode(text: str) -> str:
    """Run-length encode maximal runs of the same ASCII letter (A-Z, a-z).

    Non-letter characters pass through unchanged.
    Example: "aaabbc" -> "a3b2c1"
    """
    if not text:
        return ""

    result = []
    i = 0
    n = len(text)

    while i < n:
        char = text[i]
        # Check if it's an ASCII letter
        if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
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