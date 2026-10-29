import os
import json
from pathlib import Path


def set_init_dir(directory_path: Path) -> None:
    config_file_path = Path("conf.json")
    config_file_data = {}
    if os.path.exists(config_file_path):
        config_file_text = config_file_path.read_text()

        if config_file_text.strip():
            config_file_data = json.loads(config_file_text)

            if not isinstance(config_file_data, dict):
                raise ValueError("Conf must contain json-object")

    config_file_data["init-dir"] = str(directory_path)

    with config_file_path.open("w") as config_file:
        json.dump(config_file_data, config_file)