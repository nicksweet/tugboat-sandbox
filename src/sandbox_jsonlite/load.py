def loads(text: str) -> object:
    import json
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(str(e))