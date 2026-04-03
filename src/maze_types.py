from typing import TypeAlias
from collections import namedtuple
from enum import Enum

Cell = namedtuple("Cell", ["x", "y"])
map_type: TypeAlias = list[list[int]]


class DIRECTION(Enum):
    """
    Each wall value in the maze based on 4 bits
    determine which directions are opens.
    """

    NORTH = 0x1
    EAST = 0x2
    SOUTH = 0x4
    OUEST = 0x8
