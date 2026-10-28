import os
import tomllib
from pathlib import Path


def is_init_dir_exists() -> Path | bool:
    toml_config_path = os.path.join(os.path.curdir, "pyproject.toml")
    with open(toml_config_path, "rb") as toml:
        toml_dict = tomllib.load(toml)

    init_dir = toml_dict["app-config"]["init-dir"]

    if init_dir:
        return os.path.abspath(init_dir)
    else:
        return False;
    