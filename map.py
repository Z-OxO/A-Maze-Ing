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

def search_exit(maze: list[list[int]]) -> tuple:
    y: int = 0
    x: int = 0

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if (maze[y][x] == 17):
                return y,x

    return(-1, -1)

def print_maze(maze: list[list[int]]) -> None:
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if (maze[y][x] == 1):
                print(f"🧱", end="")
            elif (maze[y][x] == 16):
                print(f"🟩", end="")
            elif (maze[y][x] == 17):
                print(f"🟥", end="")
            else:
                print(" ", end=" ")
        print()

def main() -> None:
    maze: list[list[int]] = [
           [1,1,1,1,1,ENTRY,1,1],
           [1,0,0,0,0,0,0,1],
           [1,0,1,0,1,0,0,1],
           [1,0,1,0,1,0,1,1],
           [1,0,1,0,0,1,0,1],
           [1,0,1,0,0,0,1,1],
           [1,0,1,1,1,0,0,1],
           [1,1,1,1,1,1,1,EXIT]]
    
    print(f"{search_exit(maze)}")
    print_maze(f"{print_maze(maze)}")
    


if __name__ == "__main__":
    main()