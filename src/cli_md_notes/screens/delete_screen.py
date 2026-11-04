from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.containers import Grid
from textual.widgets import Button, Label


class DeleteScreen(ModalScreen):
    CSS_PATH = "styles.tcss"

    def __init__(self, selected_node):
        super().__init__()
        self.selected_node = selected_node

    def compose(self) -> ComposeResult:
        yield Grid(
            Label(f"Are you sure you want to delete {self.selected_node}?", id="question"),
            Button("Yes", id="yes"),
            Button("No", id="no"),
            id="delete-dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "yes":
            self.dismiss(event.button.id)
        else:
            self.app.pop_screen()