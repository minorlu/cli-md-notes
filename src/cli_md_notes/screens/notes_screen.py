from pathlib import Path

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import DirectoryTree, Header, Footer, Tree, Static


class NotesScreen(Screen):
    CSS_PATH = "styles.tcss"

    def __init__(self, notes_path: Path) -> None:
        super().__init__()
        self.notes_path = notes_path

    def compose(self) -> ComposeResult:
        yield Header()
        yield DirectoryTree(self.notes_path)
        yield Footer()

    def on_mount(self) -> None:
        self.title = f"CLI MD-Notes - {self.notes_path}"