# CLI MD Notes

##### Table of Contents
- [About](#about)
    - [Built with](#built-with)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Usage](#usage)
        - [Launching](#launching)
        - [Hotkeys](#hotkeys)
- [License](#license)

## About
CLI MD Notes is a project that seeks to use your terminal as notes editor in order to:
- Create and edit plain-texted and markdown-based notes
- Organize your notes workspace
- Provide a tool that doesn't take up much hard drive space



### Built with
- [Python 3.15](https://www.python.org/downloads/release/python-3152/)
- [Textual framework](https://textual.textualize.io/)

## Getting Started
### Prerequisites
First, you'll need to clone this repository to your computer:

```sh
git clone https://github.com/minorlu/cli-md-notes.git
```

Move into cloned repository and sync project dependencies:

```sh
cd cli-md-notes/
uv sync
```

### Usage
#### Launching
Once all the necessary conditions have been met:

```sh
uv run cli-md-notes
```

#### Hotkeys
| Key      | Action                    |
| -------- | ------------------------- |
| Arrows   | File tree navigation      |
| Space    | Expand/collapse directory |
| Enter    | Select file/directory     |
| Tab      | Change widget focus       |
| F        | Create folder             |
| M        | Create md-note            |
| P        | Create plain-text note    |
| D        | Delete note/folder        |
| Ctrl + S | Save current node         |
| C        | Change root directory     |
| Ctrl + Q | Quit the app              |

## License
This project is licensed under the MIT license. Feel free to edit and distribute this template as you like.

See [LICENSE](./LICENSE) for more information.