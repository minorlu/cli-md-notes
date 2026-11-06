import json
from pathlib import Path


def get_init_dir() -> Path | None:
    config_path = Path("conf.json")

    try:
        config_text = config_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None

    if not config_text.strip():
        return None

    config_data = json.loads(config_text)

    if not isinstance(config_data, dict):
        raise ValueError("conf.json must contain JSON-object.")

    directory = config_data.get("init-dir")

    if directory is None:
        return None

    if not isinstance(directory, str) or not directory.strip():
        raise ValueError("init-dir parameter can't be empty string")

    directory_path = Path(directory).absolute()

    if not directory_path.is_dir():
        return None

    return directory_path