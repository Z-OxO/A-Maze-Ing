# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    map.py                                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: nilinott <nilinott@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/03/17 16:10:52 by nilinott          #+#    #+#             #
#    Updated: 2026/03/17 16:10:53 by nilinott         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

ENTRY = 16
EXIT = 17
WALL = 15
TO_VISIT = 1


def search_exit(maze: list[list[int]]) -> tuple:
    y: int = 0
    x: int = 0

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if (maze[y][x] == 17):
                return y,x

    return (-1, -1)


def print_maze(maze: list[list[int]]) -> None:
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if (maze[y][x] == WALL):
                print("■", end=" ")
            elif (maze[y][x] == ENTRY):
                print("🟥", end=" ")
            elif (maze[y][x] == EXIT):
                print("🟩", end=" ")
            elif (maze[y][x] == TO_VISIT):
                print("🟧", end=" ")
            else:
                print(" ", end=" ")
        print()


def solv_search(maze: list[list[str]]) -> list[list[str]]:
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if (maze[0][7] == 0):
                maze[1][y] == 1
    return (maze)


def main() -> None:
    maze: list[list[int]] = [
           [15, 15, 15, 15, 15, 15, 15, 15],
           [15, 0, 0, 0, 0, 0, ENTRY, 15],
           [15, 0, 15, 0, 15, 0, 0, 15],
           [15, 0, 15, 0, 15, 0, 0, 15],
           [15, 0, 15, 0, 15, 15, 15, 15],
           [15, 0, 15, 0, 0, 0, 15, 15],
           [15, 0, 15, 15, 15, 0, EXIT, 15],
           [15, 15, 15, 15, 15, 15, 15, 15]]
    maze = solv_search(maze)
    print_maze(maze)


if __name__ == "__main__":
    main()