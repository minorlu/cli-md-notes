from pathlib import Path

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, TextArea, Input
from textual.containers import HorizontalGroup

from cli_md_notes.widgets import FilteredDirectoryTree
from cli_md_notes.core import (
    create_folder,
    create_file,
    delete_folder,
    delete_file,
    rename_folder
)


class NotesScreen(Screen):
    CSS_PATH = "styles.tcss"
    BINDINGS = [
        ("f", "create_folder", "Create folder"),
        ("m", "create_md", "Create md note"),
        ("p", "create_txt", "Create plain note"),
        ("d", "delete_node", "Delete"),
        ("r", "rename_node", "Rename")
    ]

    def __init__(self, notes_path: Path) -> None:
        super().__init__()
        self.notes_path = notes_path
        self.current_node_path = self.notes_path
        self.node_type = ""
        self.rename_mode = False

    def compose(self) -> ComposeResult:
        yield Header()
        yield Input(placeholder="Input node name without extension to create",
                    classes="input-hidden",
                    id="node-name-input")
        with HorizontalGroup():
            yield FilteredDirectoryTree(self.notes_path, id="notes-directory")
            yield TextArea("", id="notes-area")
        yield Footer()

    def on_mount(self) -> None:
        self.title = "CLI MD-Notes"
        self.sub_title = f"{self.notes_path}"

    def on_input_submitted(self, event: Input.Submitted, ):
        new_node_name = event.value
        if not new_node_name.strip():
            self.notify("The node name should not be empty")
            return

        if self.rename_mode:
            if self.current_node_path.is_dir():
                rename_folder(self.current_node_path, new_node_name)

            self.rename_mode = False
            self.reload_page_hide_input()
            return

        try:
            match self.node_type:
                case "folder":
                    create_folder(self.current_node_path, new_node_name)
                case "md" | "txt":
                    create_file(
                        self.current_node_path,
                        new_node_name,
                        self.node_type)
                case _:
                    self.notify("Unexpected error! Try again")
        except Exception as ex:
            self.notify(str(ex))
            return

        self.reload_page_hide_input()

    def create_node_helper(self, node_type: str) -> None:
        directory_tree = self.query_one(FilteredDirectoryTree)
        current_node = directory_tree.cursor_node
        self.current_node_path = current_node.data.path

        if not self.current_node_path.is_dir():
            self.notify("Select folder, not file!")
            return

        self.node_type = node_type
        node_name_input = self.query_one("#node-name-input")
        node_name_input.remove_class("input-hidden")

    def reload_page_hide_input(self):
        directory_tree = self.query_one("#notes-directory")
        directory_tree.reload()

        input_widget = self.query_one("#node-name-input")
        input_widget.clear()
        input_widget.add_class("input-hidden")

    def action_create_folder(self) -> None:
        self.create_node_helper("folder")

    def action_create_md(self) -> None:
        self.create_node_helper("md")

    def action_create_txt(self) -> None:
        self.create_node_helper("txt")

    def action_delete_node(self) -> None:
        directory_tree = self.query_one(FilteredDirectoryTree)
        current_node = directory_tree.cursor_node
        self.current_node_path = current_node.data.path

        if self.current_node_path.is_dir():
            delete_folder(self.current_node_path)
        else:
            delete_file(self.current_node_path)

        directory_tree = self.query_one("#notes-directory")
        directory_tree.reload()

    def action_rename_node(self) -> None:
        directory_tree = self.query_one(FilteredDirectoryTree)
        current_node = directory_tree.cursor_node
        self.current_node_path = current_node.data.path

        self.rename_mode = True

        node_name_input = self.query_one("#node-name-input")
        node_name_input.remove_class("input-hidden")
