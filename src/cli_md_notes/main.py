from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.binding import Binding
from textual.reactive import reactive

from cli_md_notes.screens.choosepathscreen import ChoosePathScreen


class CliMdNotesApp(App):
    CSS_PATH = "styles.tcss"
    SCREENS = {"choose_path_screen": ChoosePathScreen}

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def on_mount(self) -> None:
        self.title = "CLI MD-Notes"
        self.theme = "tokyo-night"
        self.push_screen("choose_path_screen", callback=self.receive_path)

    def receive_path(self, path: Path | None) -> None:
        if path is None:
            return

        self.notify(f"{path}")

if __name__ == "__main__":
    app = CliMdNotesApp()
    app.run()

