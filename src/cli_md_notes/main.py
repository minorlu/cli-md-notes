from json import JSONDecodeError
from pathlib import Path

from textual.app import App
from textual.screen import ModalScreen

from .screens import ChoosePathScreen, NotesScreen
from .utils import get_init_dir, set_init_dir


class CliMdNotesApp(App):
    CSS_PATH = "styles.tcss"

    notes_path = None
    initial_dir = Path("/")

    def on_mount(self) -> None:
        self.title = "CLI MD-Notes"
        self.app.theme = "tokyo-night"
        try:
            self.initial_dir = get_init_dir()
        except (OSError, ValueError) as er:
            self.notify(
                f"Error when opening initial directory from config: {er}"
                )
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

    def action_quit(self) -> None:
        if isinstance(self.screen, ModalScreen):
            return

        if isinstance(self.screen, NotesScreen):
            self.screen.request_quit()
        else:
            self.exit()

def main():
    app = CliMdNotesApp()
    app.run()

if __name__ == "__main__":
    main()
