import json


def dumps(obj: object) -> str:
    """Serialize an object to a compact, deterministic JSON string."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))