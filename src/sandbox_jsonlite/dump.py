import json

def dumps(obj: object) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))