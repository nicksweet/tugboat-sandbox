import json


def dumps(obj: object) -> str:
    """Serialize Python object to compact JSON with sorted keys."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))