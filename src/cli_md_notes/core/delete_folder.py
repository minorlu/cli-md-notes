import os
import shutil
from pathlib import Path

def delete_folder(folder_path: Path) -> None:
    if not os.path.exists(folder_path):
        raise Exception("This folder does not exist.")
    
    shutil.rmtree(folder_path)