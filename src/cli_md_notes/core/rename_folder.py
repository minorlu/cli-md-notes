import os

from pathlib import Path


def rename_folder(folder_path: Path, new_folder_name: str) -> None:
    path_parent = folder_path.parent
    new_folder_path = path_parent / new_folder_name

    os.rename(folder_path, new_folder_path)