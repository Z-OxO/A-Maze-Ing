directions = [
    (0, -1, 'N'),
    (1, 0, 'E'),
    (0, 1, 'S'),
    (-1, 0, 'W')
]


def direction_maze(cell, direction):
    if (direction == 'N'):
        return not (cell & 1)
    if (direction == 'E'):
        return not (cell & 2)
    if (direction == 'S'):
        return not (cell & 4)
    if (direction == 'W'):
        return not (cell & 8)


def exit_maze(x, y, width, height, start):
    if ((x, y) == start):
        return (False)
    return (x == 0 or y == 0 or x == width - 1 or y == height - 1)


def solver_back(maze, x, y, visited, path, start):
    width = len(maze[0])
    height = len(maze)

    if ((x, y) in visited):
        return (False)

    visited.add((x, y))
    path.append((x, y))

    if (exit_maze(x, y, width, height, start)):
        return (True)

    cell = maze[y][x]

    for dx, dy, d in directions:
        if (direction_maze(cell, d)):
            nx, ny = x + dx, y + dy

            if (0 <= nx < width and 0 <= ny < height):
                if (solver_back(maze, nx, ny, visited, path, start)):
                    return (True)
    path.pop()
    return (False)


def path_to_moves(path):
    moves = ""

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


def solve_maze(maze, start_x, start_y):
    visited = set()
    path = []

    if (solver_back(maze, start_x, start_y, visited, path, (start_x, start_y))):
        return (path_to_moves(path))
    return (None)


if __name__ == "__main__":
    maze = [
        [15, 7, 15, 15, 15],
        [15, 9, 5, 1, 15],
        [15, 8, 1, 2, 15],
        [15, 4, 1, 2, 15],
        [15, 4, 1, 8, 15]
    ]

    start_x, start_y = 1, 1

    result = solve_maze(maze, start_x, start_y)

    if result:
        print("Path:", result)
    else:
        print("No solution found")
