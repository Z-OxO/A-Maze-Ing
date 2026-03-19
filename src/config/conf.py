class Conf():
    def __init__(self, width: int, height: int, output_file: str):
        self.__width = width
        self.__height = height
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
