import sys


class Conf():
    def __init__(self,
                 width: int, height: int,
                 output_file: str,
                 entry: tuple[int, int], exit_maze: tuple[int, int],
                 perfect: bool):
        self.__width = width
        self.__height = height
        self.__entry = entry
        self.__exit_maze = exit_maze
        self.__perfect = perfect

        if (output_file == "None"):
            raise ValueError("'OUTPUT_FILE' not found !")
        else:
            self.__output_file = output_file

    def get_width(self) -> int:
        return (self.__width)

    def get_height(self) -> int:
        return (self.__height)

    def get_output_file(self) -> str:
        return (self.__output_file)

    def get_entry(self) -> tuple[int, int]:
        return (self.__entry)

    def get_exit_maze(self) -> tuple[int, int]:
        return (self.__exit_maze)

    def get_perfect(self) -> bool:
        return (self.__perfect)


def get_value(key: str) -> str | None:
    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                line = line.strip()

                if (line.startswith(key)):
                    parts = line.split("=")
                    if (len(parts) == 2):
                        return (parts[1].strip())
    except FileNotFoundError:
        raise ValueError("File not found !")
    return (None)


def parsing() -> None:
    if (len(sys.argv) < 2):
        print("Error !")
        return
    try:
        width_str: str = str(get_value("WIDTH"))
        height_str: str = str(get_value("HEIGHT"))
        output_file_str: str = str(get_value("OUTPUT_FILE"))
        entry_str: str = str(get_value("ENTRY"))
        exit_maze_str: str = str(get_value("EXIT"))
        perfect_str: str = str(get_value("PERFECT"))

        if (None in (width_str, height_str, output_file_str,
                     entry_str, exit_maze_str, perfect_str)):
            raise ValueError("Missing keys")

        if (entry_str.count(',') != 1) or (exit_maze_str.count(',')) != 1:
            raise ValueError("ENTRY or EXIT must be in format 'x,y'")

        if (entry_str == exit_maze_str):
            raise ValueError("The inlet must not be "
                             "in the same place as the outlet.")

        width: int = int(width_str)
        height: int = int(height_str)
        output_file: str = (output_file_str)

        entry: tuple[int, int] = tuple(map(int, entry_str.split(',')))
        exit_maze: tuple[int, int] = tuple(map(int, exit_maze_str.split(',')))

        if (perfect_str == "True"):
            perfect: bool = True
        elif (perfect_str == "False"):
            perfect = False
        else:
            raise ValueError("Invalid PERFECT value")

        value: Conf = Conf(width, height, output_file, entry, exit_maze,
                           perfect)

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    parsing()
