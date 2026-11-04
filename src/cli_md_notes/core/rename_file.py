import os

from pathlib import Path


def rename_file(file_path: Path, new_file_name: str) -> None:
    if (new_file_name in {".", ".."}
        or "/" in new_file_name
        or "\\" in new_file_name):
        raise ValueError("Enter correct folder name.")

    file_extension = os.path.splitext(file_path)[1]
    path_parent = file_path.parent
    new_file_path = path_parent / f"{new_file_name}{file_extension}"

    if os.path.exists(new_file_path):
        raise FileExistsError("This file already exists in selected directory.")

    os.rename(file_path, new_file_path)