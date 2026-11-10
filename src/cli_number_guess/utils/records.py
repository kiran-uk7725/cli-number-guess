import json
from pathlib import Path
from typing import Any

def load_records(path: Path, encoding="utf-8") -> dict[str, Any]:
    """Return saved best scores, or {} if none are usable."""

    if not path.is_file():
        return {}

    try:
        return json.loads(path.read_text(encoding=encoding))
    except (json.JSONDecodeError, PermissionError):
        return {}


def save_records(path: Path, records: dict[str, Any]) -> None:
    """Write best scores to disk as JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    json_data = json.dumps(records, indent=4)

    path.write_text(json_data)