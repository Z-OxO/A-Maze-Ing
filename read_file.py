# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    read_file.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: nilinott <nilinott@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/03/18 17:41:06 by nilinott          #+#    #+#             #
#    Updated: 2026/03/18 17:41:07 by nilinott         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys
from src.config.conf import Conf


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


def add_conf() -> str:
    if (len(sys.argv) < 2):
        print("Error !")
        return
    try:
        width: int = int(get_value("WIDTH"))
        height: int = int(get_value("HEIGHT"))
        output_file: str = str(get_value("OUTPfUT_FILE"))
        value: Conf = Conf(width, height, output_file)
    except TypeError:
        print("Error: Key not found !")
        return
    return (value)


if __name__ == "__main__":
    add_conf()
