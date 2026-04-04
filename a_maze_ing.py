from src.tui_render import TUIRenderer
from src.conf import Config
from mazegen import Maze

import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("File argument not found!\nUsage: a_maze_ing.py config.txt")
        sys.exit(0)
    try:
        print(sys.argv[0])
        cfg = Config(sys.argv[1])
    except (ValueError, FileNotFoundError) as e:
        print(f"Error during parsing: {e}")
    m = Maze(cfg)
    renderer = TUIRenderer(m)
    renderer.run()
