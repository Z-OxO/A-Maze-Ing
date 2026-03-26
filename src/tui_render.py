import readchar
from rich.console import Console, Group
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from mazegen.maze import Maze
from src.types import Cell, DIRECTION


_PALETTES: list[tuple[str, str]] = [
    ("bright_white",  "Classic"),
    ("cyan",          "Ocean"),
    ("yellow",        "Gold"),
    ("magenta",       "Neon"),
    ("bright_green",  "Matrix"),
]


class TUIRenderer:
    """Terminal UI renderer for A-Maze-ing.

    Args:
        maze: The Maze instance to render.

    Usage::
        renderer = TUIRenderer(maze)
        renderer.on_toggle_path = lambda: your_solver.toggle()
        renderer.run()
    """

    def __init__(self, maze: Maze) -> None:
        self.console = Console()
        self._maze = maze

        self._path_visible: bool = False
        self._palette_idx: int = 0
        self._running: bool = True
        self._status: str = "Ready"

        self.WALL = "██"
        self.PATH = "  "
        self.START = "[bold green]██[/]"
        self.END = "[bold red]██[/]"

        self.on_toggle_path = lambda: None
        self.on_solve = lambda: None

    def run(self) -> None:
        """Start the blocking render + input loop."""
        with Live(
            self._build_renderable(),
            console=self.console,
            refresh_per_second=4,
            screen=True,
            vertical_overflow="visible",
        ) as live:
            while self._running:
                key = readchar.readkey()
                self._handle_key(key)
                live.update(self._build_renderable())

    def _handle_key(self, key: str) -> None:
        match key:
            case "r" | "R":
                self._status = "Generating..."
                self._maze.gen()
                self._path_visible = False
                self._status = "New maze generated"
            case "p" | "P":
                self._path_visible = not self._path_visible
                self.on_toggle_path()
                self._status = "Path ON" if self._path_visible else "Path OFF"
            case "c" | "C":
                self._palette_idx = (self._palette_idx + 1) % len(_PALETTES)
                _, name = _PALETTES[self._palette_idx]
                self._status = f"Color -> {name}"
            case "q" | "Q" | readchar.key.CTRL_C:
                self._running = False

    def _build_renderable(self) -> Panel:
        """Assemble the full UI as a single centered Panel."""
        color, _ = _PALETTES[self._palette_idx]

        inner = Group(
            self._render_maze(color),
            Text(""),
            self._render_menu(color),
        )

        return Panel(
            inner,
            title=f"[bold {color}]A-Maze-ing[/]",
            subtitle=f"[dim italic]{self._status}[/]",
            border_style=color,
            padding=(1, 4),
            expand=False,
        )

    def _render_maze(self, color: str) -> Text:
        """Build the ASCII grid as a Rich Text object."""
        W, H = self._maze.width, self._maze.height

        ascii_map: list[list[str]] = [
            [f"[{color}]"+self.WALL+"[/]"] * (2 * W + 1) for _ in range(2 * H + 1)
        ]

        for y in range(H):
            for x in range(W):
                cell_hex: int = self._maze.map_[y][x]

                if Cell(x, y) in self._maze.pattern:
                    ascii_map[2 * y + 1][2 * x + 1] = (
                        "[bold blue]" + self.WALL + "[/]"
                    )
                else:
                    ascii_map[2 * y + 1][2 * x + 1] = self.PATH

                if not (cell_hex & DIRECTION.NORTH.value):
                    ascii_map[2 * y][2 * x + 1] = self.PATH
                if not (cell_hex & DIRECTION.EAST.value):
                    ascii_map[2 * y + 1][2 * x + 2] = self.PATH
                if not (cell_hex & DIRECTION.SOUTH.value):
                    ascii_map[2 * y + 2][2 * x + 1] = self.PATH
                if not (cell_hex & DIRECTION.OUEST.value):
                    ascii_map[2 * y + 1][2 * x] = self.PATH

        if hasattr(self._maze, "entry") and self._maze.entry:
            ex, ey = self._maze.entry.x, self._maze.entry.y
            ascii_map[2 * ey + 1][2 * ex + 1] = f"[bold green]{self.WALL}[/]"

        if hasattr(self._maze, "exit_") and self._maze.exit_:
            ex, ey = self._maze.exit_.x, self._maze.exit_.y
            ascii_map[2 * ey + 1][2 * ex + 1] = f"[bold red]{self.WALL}[/]"

        raw = "\n".join("".join(row) for row in ascii_map)
        return Text.from_markup(raw, justify="center")

    def _render_menu(self, color: str) -> Table:
        """Build the key-binding bar as a centered grid table."""
        table = Table.grid(expand=False, padding=(0, 3))
        for _ in range(4):
            table.add_column(justify="center")

        path_label = "Path ON" if self._path_visible else "Path OFF"
        _, palette_name = _PALETTES[self._palette_idx]

        table.add_row(
            self._key("R", "Regen",      color),
            self._key("P", path_label,   color),
            self._key("C", palette_name, color),
            self._key("Q", "Quit",       color),
        )
        return table

    @staticmethod
    def _key(k: str, label: str, color: str) -> Text:
        """Format a single key badge + label."""
        t = Text()
        t.append(f" {k} ", style=f"bold black on {color}")
        t.append(f" {label}", style="dim")
        return t
