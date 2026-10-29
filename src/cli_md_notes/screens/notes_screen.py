from pathlib import Path

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, TextArea, Input
from textual.containers import HorizontalGroup

from cli_md_notes.widgets import FilteredDirectoryTree


class NotesScreen(Screen):
    CSS_PATH = "styles.tcss"
    BINDINGS = [
        ("f", "create_folder", "Create folder")
    ]

    def __init__(self, notes_path: Path) -> None:
        super().__init__()
        self.notes_path = notes_path

    def compose(self) -> ComposeResult:
        yield Header()
        yield Input(placeholder="Input folder name to create", classes="input-hidden")
        with HorizontalGroup():
            yield FilteredDirectoryTree(self.notes_path, id="notes-directory")
            yield TextArea("", id="notes-area")
        yield Footer()

    def on_mount(self) -> None:
        self.title = "CLI MD-Notes"
        self.sub_title = f"{self.notes_path}"

    def action_create_folder(self) -> None:
        directory_tree = self.query_one(FilteredDirectoryTree)
        current_node = directory_tree.cursor_node
        current_node_path = current_node.data.path

        folder_name_input = self.query_one("Input.input-hidden")
        folder_name_input.remove_class("input-hidden")
