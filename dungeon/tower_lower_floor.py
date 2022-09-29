import dungeon.tower_entrance
import dungeon.tower_upper_floor
import dungeon.tower_basement
from functions import typing, convert_to_int, check_option_validity
from plants import purple_moss


def introduction(character, world):
    if world.get_purple_moss():
        purple_moss(character)
    typing("You see a small circular room, dark and cold. \
    Stairs to your right spiral up to the upper floor.\
    Stairs to your left spiral down into the earth.")
    if world.get_purple_moss():
        typing("A large patch of purple moss grows on the far wall.")
    lower_floor_options(character, world)


def lower_floor_options(character, world):
    if 'flint and steel' in character.equipment and world.get_purple_moss():
        x = convert_to_int(input(typing('''Would you like to:
                1 - take the stairs up
                2 - take the stairs down
                3 - leave the tower
                4 - set fire to the purple moss
                ''')))
        if not check_option_validity(x, [1, 2, 3, 4]):
            typing("That is not a valid option")
            lower_floor_options(character, world)
    else:
        x = convert_to_int(input(typing('''Would you like to:
                1 - take the stairs up
                2 - take the stairs down
                3 - leave the tower
                ''')))
        if not check_option_validity(x, [1, 2, 3]):
            typing("That is not a valid option")
            lower_floor_options(character, world)
    if x == 1:
        tower_upper_floor.introduction(character, world)
    if x == 2:
        tower_basement.introduction(character, world)
    if x == 3:
        tower_entrance.introduction(character, world)
    if x == 4:
        set_fire_to_the_moss(character, world)


def set_fire_to_the_moss(character, world):
    typing("You strike your flint and steel against a patch of the purple moss.\
           With a loud whoosh it instantly catches alight, the fire racing across it.\
           The fire blasts you back a few feet, hurting you.\
           You gingerly get to your feet, pleased to note that the purple moss is gone.")
    world.set_purple_moss(False)
    lower_floor_options(character, world)

