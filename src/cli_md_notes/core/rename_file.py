import os

from pathlib import Path


def rename_file(file_path: Path, new_file_name: str) -> None:
    file_extension = os.path.splitext(file_path)[1]
    path_parent = file_path.parent
    new_file_path = path_parent / f"{new_file_name}{file_extension}"

    os.rename(file_path, new_file_path)