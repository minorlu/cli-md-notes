from pathlib import Path

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import DirectoryTree, Header, Footer, Tree, Static
from textual.containers import HorizontalGroup

from cli_md_notes.widgets.filtered_directory_tree import FilteredDirectoryTree

class NotesScreen(Screen):
    CSS_PATH = "styles.tcss"

    def __init__(self, notes_path: Path) -> None:
        super().__init__()
        self.notes_path = notes_path

    def compose(self) -> ComposeResult:
        yield Header()
        with HorizontalGroup():
            yield FilteredDirectoryTree(self.notes_path, id="notes-directory")
            yield Static("Notes area", id="notes-area")
        yield Footer()

    def on_mount(self) -> None:
        self.title = "CLI MD-Notes"
        self.sub_title = f"{self.notes_path}"