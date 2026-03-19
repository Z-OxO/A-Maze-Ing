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
