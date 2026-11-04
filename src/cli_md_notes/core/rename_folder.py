import os

from pathlib import Path


def rename_folder(folder_path: Path, new_folder_name: str) -> Path:
    if (new_folder_name in {".", ".."}
        or "/" in new_folder_name
        or "\\" in new_folder_name):
        raise ValueError("Enter correct folder name.")

    path_parent = folder_path.parent
    new_folder_path = path_parent / new_folder_name

    if os.path.exists(new_folder_path):
        raise FileExistsError(
            "This folder already exists in selected directory."
            )

    os.rename(folder_path, new_folder_path)
    
    return new_folder_path