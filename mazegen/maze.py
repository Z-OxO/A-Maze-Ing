from random import Random
from src.types import Cell, map_type
from src.conf import Config


class Maze:
    def __init__(self, cfg: Config):
        self.width: int = cfg.width
        self.height: int = cfg.height
        self.map_: map_type = self._init_map()
        self.random = Random(cfg.seed)
        self.entry = cfg.entry
        self.exit_ = cfg.exit_
        self.pattern = self._create_pattern()  # 42 pattern relative pos
        self._DIRS_OFFSETS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def __str__(self) -> str:
        return "\n".join("".join(f"{c:X}" for c in row) for row in self.map_)

    def _init_map(self) -> map_type:
        return [[0xF] * self.width for _ in range(self.height)]

    def _create_pattern(self) -> set[Cell]:
        """
        Return the set of Cell that compose the 42 pattern
        based on the maze.
        """
        if self.height < 10 or self.width < 10:
            return set()

        offset_x = self.height // 2 - 2
        offset_y = self.width // 2 - 3

        # Pattern 42 absolute pos
        pattern_42_pos = [
            (0, 0),
            (1, 0),
            (2, 0),
            (2, 1),
            (2, 2),
            (3, 2),
            (4, 2),
            (0, 4),
            (0, 5),
            (0, 6),
            (1, 6),
            (2, 6),
            (2, 5),
            (2, 4),
            (3, 4),
            (4, 4),
            (4, 5),
            (4, 6),
        ]

        cells = {Cell(offset_y + y, offset_x + x) for x, y in pattern_42_pos}

        if self.entry in cells or self.exit_ in cells:
            return set()
        return cells

    def _get_neighbor(self, visited: set[Cell], curr: Cell) -> list[Cell]:
        """Return unvisited neighbours of curr within maze bounds."""
        neighbor = [
            Cell(curr.x, curr.y - 1),  # N
            Cell(curr.x + 1, curr.y),  # E
            Cell(curr.x, curr.y + 1),  # S
            Cell(curr.x - 1, curr.y),  # O
        ]
        return [
            c
            for c in neighbor
            if 0 <= c.x < self.width
            and 0 <= c.y < self.height
            and c not in visited
        ]

    def _create_wall(self, curr_cell: Cell, next_cell: Cell) -> None:
        dx, dy = next_cell.x - curr_cell.x, next_cell.y - curr_cell.y
        bit = self._DIRS_OFFSETS.index((dx, dy))
        self.map_[curr_cell.y][curr_cell.x] &= ~(1 << bit)
        self.map_[next_cell.y][next_cell.x] &= ~(1 << (bit ^ 2))

    def gen(self) -> None:
        self.map_: map_type = self._init_map()
        visited: set[Cell] = set()
        stack: list[Cell] = [self.entry]
        visited.add(self.entry)
        visited.update(self.pattern)

        while stack:
            neighbor_available = self._get_neighbor(visited, stack[-1])
            if not neighbor_available:
                stack.pop()
                continue

            next_idx = int(self.random.random() * len(neighbor_available))
            next_cell = neighbor_available[next_idx]
            self._create_wall(stack[-1], next_cell)
            visited.add(next_cell)
            stack.append(next_cell)

