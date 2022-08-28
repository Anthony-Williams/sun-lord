import os
from time import sleep

import functions
import tower_entrance
import village
from hero_class import Hero


def main():
    character = functions.create_character()
    functions.clear_screen()
    village.introduction(character)
    functions.equip(character)
    world = functions.create_world()
    world.set_new_weather()
    tower_entrance.introduction(character, world)


if __name__ == "__main__":
    main()
