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
            print("Error: 'OUTPUT_FILE' not found !")
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


def get_value(key) -> str | None:
    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                line = line.strip()

                if (line.startswith(key)):
                    parts = line.split("=")
                    if (len(parts) == 2):
                        return (parts[1].strip())
    except FileNotFoundError:
        pass
    return (None)


def parsing() -> None:
    if (len(sys.argv) < 2):
        print("Error !")
        return
    try:
        width: int = int(get_value("WIDTH"))
        height: int = int(get_value("HEIGHT"))
        output_file: str = str(get_value("OUTPUT_FILE"))
        entry: tuple[int, int] = (get_value("ENTRY"))
        entry.split(',')
        exit_maze: tuple[int, int] = get_value("EXIT")
        exit_maze.split(',')
        perfect: bool = (True if get_value("PERFECT") == "True" else
                         (False if get_value("PERFECT") == "False" else None))
        if (perfect is None):
            print("Error : perfect key !")
            return (None)
        value: Conf = Conf(width, height, output_file, entry, exit_maze,
                           perfect)
        print(value.get_entry())
    except (TypeError, ValueError):
        print("Error: Key not found or value error !")
        return


if __name__ == "__main__":
    parsing()
