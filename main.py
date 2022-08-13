import os
from time import sleep

import functions
import tower_entrance
from hero_class import Hero


def main():
    character = functions.create_character()
    functions.clear_screen()
    # todo
    # village.shopping()
    tower_entrance.introduction(character)


if __name__ == "__main__":
    main()
