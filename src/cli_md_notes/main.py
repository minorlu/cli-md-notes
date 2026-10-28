from pathlib import Path

from textual.app import App

from .screens import ChoosePathScreen
from .screens import NotesScreen
from .utils import is_init_dir_exists


class CliMdNotesApp(App):
    CSS_PATH = "styles.tcss"

    notes_path: Path | None = None

    def on_mount(self) -> None:
        self.title = "CLI MD-Notes"
        self.app.theme = "tokyo-night"
        self.push_screen(ChoosePathScreen(), callback=self.receive_path)

    def receive_path(self, path: Path | None) -> None:
        if path is None:
            return

        self.notes_path = path
        self.push_screen(NotesScreen(self.notes_path))

if __name__ == "__main__":
    app = CliMdNotesApp()
    app.run()

