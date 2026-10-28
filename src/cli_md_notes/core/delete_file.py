import os
from pathlib import Path

def delete_file(file_path: Path) -> None:
    if not os.path.exists(file_path):
        raise Exception("This file does not exist.")
    
    os.remove(file_path)