from collections import deque

directions = [
    (0, -1, 'N'),
    (1, 0, 'E'),
    (0, 1, 'S'),
    (-1, 0, 'W')
]
# Check Wall


def direction_maze(cell, direction):
    if (direction == 'N'):
        return not (cell & 1)
    if (direction == 'E'):
        return not (cell & 2)
    if (direction == 'S'):
        return not (cell & 4)
    if (direction == 'W'):
        return not (cell & 8)


def can_move(maze: list[list[int]], x, y, nx, ny, direction):
    cell = maze[y][x]

    if (not direction_maze(cell, direction)):
        return (False)

    opposite: dict[str, str] = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    neighbor: int = maze[ny][nx]

    return (direction_maze(neighbor, opposite[direction]))


def solver_back(maze: list[list[int]], start, end):
    width: int = (len(maze))
    height: int = len(maze)

    queue = deque()
    queue.append((start, [start]))

    visited = set()
    visited.add(start)

    while (queue):
        (x, y), path = queue.popleft()

        if ((x, y) == end):
            return (path)

        for dx, dy, d in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < width and 0 <= ny < height):
                if (can_move(maze, x, y, nx, ny, d)):
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((((nx, ny), path + [(nx, ny)])))
    return (None)


def path_to_moves(path):
    moves: str = ""

    for i in range(1, len(path)):
        x1, y1 = path[i - 1]
        x2, y2 = path[i]

        if x2 == x1 + 1:
            moves += 'E'
        elif x2 == x1 - 1:
            moves += 'W'
        elif y2 == y1 + 1:
            moves += 'S'
        elif y2 == y1 - 1:
            moves += 'N'

    return moves


def display_maze_ascii(maze, path=None, start=None, end=None):
    height = len(maze)
    width = len(maze[0])
    path_set = set(path) if path else set()

    for y in range(height):
        # ligne supérieure
        line = ""
        for x in range(width):
            cell = maze[y][x]
            line += "┌" if cell & 1 else " "  # haut
            line += "─" if cell & 2 else " "  # droite
        print(line)

        # ligne centrale
        line = ""
        for x in range(width):
            if (x, y) == start:
                line += "S"
            elif (x, y) == end:
                line += "E"
            elif (x, y) in path_set:
                line += "·"
            else:
                line += " "
            line += "│" if maze[y][x] & 2 else " "
        print(line)

        # ligne inférieure
        line = ""
        for x in range(width):
            line += "└" if maze[y][x] & 4 else " "
            line += "─" if maze[y][x] & 8 else " "
        print(line)
    print()


if __name__ == "__main__":

    maze = [
        [15, 15, 15, 15, 15],
        [15, 9, 5, 1, 15],
        [15, 8, 1, 2, 15],
        [15, 4, 1, 8, 15],
        [15, 8, 8, 8, 15]
    ]

start = (1, 1)
end = (2, 4)

path = solver_back(maze, start, end)
display_maze_ascii(maze, path, start, end)

if path:
    moves = ''.join(
        'E' if path[i+1][0] > path[i][0] else
        'W' if path[i+1][0] < path[i][0] else
        'S' if path[i+1][1] > path[i][1] else
        'N' for i in range(len(path)-1)
    )
    print("Path moves:", moves)
