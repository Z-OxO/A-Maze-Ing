from typing import TypeAlias
from collections import namedtuple
from random import choices
from enum import Enum

Cell = namedtuple("Cell", ["x", "y"])
map_type: TypeAlias = list[list[int]]


class DIRECTION(Enum):
    NORTH = 0x1
    EAST = 0x2
    SOUTH = 0x4
    OUEST = 0x8


class Maze:
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.map: map_type = self._init_map()
        self._DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def __repr__(self) -> str:
        return "\n".join("".join(f"{c:X}" for c in row) for row in self.map)

    def _init_map(self) -> map_type:
        return [[0xF] * self.width for _ in range(self.height)]

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
        bit = self._DIRS.index((dx, dy))
        self.map[curr_cell.y][curr_cell.x] &= ~(1 << bit)
        self.map[next_cell.y][next_cell.x] &= ~(1 << (bit ^ 2))

    def gen(self) -> None:
        visited: set[Cell] = set()
        stack: list[Cell] = [Cell(0, 0)]
        visited.add(Cell(0, 0))

        while stack:
            neighbor_available = self._get_neighbor(visited, stack[-1])
            if not neighbor_available:
                stack.pop()
                continue

            next_cell = choices(neighbor_available)[0]
            self._create_wall(stack[-1], next_cell)
            visited.add(next_cell)
            stack.append(next_cell)
