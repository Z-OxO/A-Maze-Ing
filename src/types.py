from typing import TypeAlias
from collections import namedtuple
from enum import Enum

Cell = namedtuple("Cell", ["x", "y"])
map_type: TypeAlias = list[list[int]]


class DIRECTION(Enum):
    NORTH = 0x1
    EAST = 0x2
    SOUTH = 0x4
    OUEST = 0x8
