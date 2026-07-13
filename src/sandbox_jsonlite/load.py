import json


def loads(text: str) -> object:
    """Parse JSON text and return the corresponding Python object.

    Args:
        text: A string containing JSON data.

    Returns:
        The Python object represented by the JSON text.

    Raises:
        ValueError: If the input text is not valid JSON.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}") from e