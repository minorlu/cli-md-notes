import os
from pathlib import Path


def create_file(path: Path, file_name: str, file_extension: str) -> Path | None:
    full_file_name = f"{file_name}.{file_extension}"
    new_path = os.path.join(path, full_file_name)
    if os.path.exists(new_path):
        raise Exception("This file already exists in selected directory.")

    file = open(new_path, "x")
    return new_path
    