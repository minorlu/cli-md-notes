import os
from pathlib import Path


def create_folder(path: Path, folder_name: str) -> Path | None:
    if (folder_name in {".", ".."}
        or "/" in folder_name
        or "\\" in folder_name):
        raise ValueError("Enter correct folder name.")
    
    new_path = path / folder_name
    if os.path.exists(new_path):
        raise FileExistsError(
            "This folder already exists in selected directory."
            )

    os.mkdir(new_path)
    return new_path