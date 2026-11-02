from pathlib import Path


def get_file_type(file_path: Path) -> str:
    return file_path.name.split(".")[-1]