import os
from pathlib import Path


def create_file(path: Path, file_name: str, file_extension: str) -> Path | None:
    if (file_name in {".", ".."}
        or "/" in file_name
        or "\\" in file_name):
        raise ValueError("Enter correct folder name.")
    
    full_file_name = f"{file_name}.{file_extension}"
    new_path = path / full_file_name
    if os.path.exists(new_path):
        raise FileExistsError("This file already exists in selected directory.")

    file = open(new_path, "x")
    return new_path
    