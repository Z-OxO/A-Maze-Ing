from rich.console import Console
from mazegen.maze import Maze
from src.types import Cell, DIRECTION


class TUIRenderer:
    def __init__(self, maze: Maze):
        self.console = Console()
        self._maze = maze
        self._DIR = DIRECTION

        self.WALL = "██"
        self.PATH = "  "
        self.START = "[bold green]██[/]"
        self.END = "[bold red]██[/]"

    def _map_to_ascii(self) -> str:
        W, H = self._maze.width, self._maze.height

        ascii_map: list[str] = [["██"] * (2 * W + 1) for _ in range(2 * H + 1)]
        for y in range(H):
            for x in range(W):
                cell: Cell = self._maze.map[y][x]
                ascii_map[2 * y + 1][2 * x + 1] = self.PATH

                if not (cell & DIRECTION.NORTH.value):
                    ascii_map[2 * y][2 * x + 1] = self.PATH  # N open
                if not (cell & DIRECTION.EAST.value):
                    ascii_map[2 * y + 1][2 * x + 2] = self.PATH  # E open
                if not (cell & DIRECTION.SOUTH.value):
                    ascii_map[2 * y + 2][2 * x + 1] = self.PATH  # S open
                if not (cell & DIRECTION.OUEST.value):
                    ascii_map[2 * y + 1][2 * x] = self.PATH  # O open

        if hasattr(self._maze, 'entry') and self._maze.entry:
            ex, ey = self._maze.entry.x, self._maze.entry.y
            ascii_map[2 * ey + 1][2 * ex + 1] = self.START

        if hasattr(self._maze, 'exit_') and self._maze.exit_:
            ex, ey = self._maze.exit_.x, self._maze.exit_.y
            ascii_map[2 * ey + 1][2 * ex + 1] = self.END

        return "\n".join("".join(row) for row in ascii_map)

    def render(self) -> None:
        maze_output = self._map_to_ascii()
        self.console.print(maze_output)
