from pathlib import Path

from textual.app import App

from .screens import ChoosePathScreen, NotesScreen
from .utils import get_init_dir, set_init_dir


class CliMdNotesApp(App):
    CSS_PATH = "styles.tcss"

    notes_path = None
    initial_dir = Path("/")

    def on_mount(self) -> None:
        self.title = "CLI MD-Notes"
        self.app.theme = "tokyo-night"
        self.initial_dir = get_init_dir()
        if not self.initial_dir:
            self.push_screen(ChoosePathScreen(), callback=self.receive_path)
        else:
            self.push_screen(NotesScreen(self.initial_dir))

    def receive_path(self, path: Path | None) -> None:
        if path is None:
            return

        self.notes_path = path
        set_init_dir(self.notes_path)
        self.push_screen(NotesScreen(self.notes_path))
        

def main():
    app = CliMdNotesApp()
    app.run()

if __name__ == "__main__":
    main()
