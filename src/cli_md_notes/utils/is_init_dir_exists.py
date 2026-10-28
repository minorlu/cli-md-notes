import os
import tomllib


def is_init_dir_exists() -> bool:
    toml_config_path = os.path.abspath(os.path.curdir(), "pyproject.toml")
    with open(toml_config_path, "r") as toml:
        toml_dict = tomllib.load(toml)

    
    