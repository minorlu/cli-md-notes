import os
import json
from pathlib import Path


def get_init_dir() -> Path | bool:
    config_file_path = os.path.join(os.path.curdir, "conf.json")
    if not os.path.exists(config_file_path):
        return False

    with open(config_file_path, "r") as config_file:
        if config_file.read() == "":
            return False
        
        config_file.seek(0)
        config_data = json.load(config_file)

    if not "init-dir" in config_data:
        return False

    return os.path.abspath(config_data["init-dir"])
    