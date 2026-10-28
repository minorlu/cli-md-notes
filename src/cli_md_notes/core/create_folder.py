import os
from pathlib import Path


def create_folder(path: Path, folder_name: str) -> Path | None:
    new_path = os.path.join(path, folder_name)
    if os.path.exists(new_path):
        raise Exception("This folder already exists in selected directory.")

    os.makedirs(new_path)
    return new_path