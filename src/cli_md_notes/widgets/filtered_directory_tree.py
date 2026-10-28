import os
from pathlib import Path
from typing import Iterable

from textual.widgets import DirectoryTree


class FilteredDirectoryTree(DirectoryTree):
    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        filtered_paths: Iterable[Path] = []
        for path in paths:
            if os.path.isdir(path)\
               or path.name.endswith(".md")\
               or path.name.endswith(".txt"):
                filtered_paths.append(path)

        return filtered_paths