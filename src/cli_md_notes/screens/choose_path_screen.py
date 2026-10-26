from pathlib import Path

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import DirectoryTree, Header, Footer, Static


class ChoosePathScreen(Screen[Path]):
    CSS_PATH = "styles.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(
            "Select your notes folder (space -> expand/collapse, enter -> select)"
            )
        yield DirectoryTree(Path.home())
        yield Footer()

    def on_directory_tree_directory_selected(
        self,
        message: DirectoryTree.DirectorySelected
    ) -> None:
        self.dismiss(message.path)