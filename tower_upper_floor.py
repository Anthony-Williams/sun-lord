import tower_lower_floor
from functions import typing, convert_to_int, check_option_validity
import actions


def upper_floor_options(character):
    typing('''The roof has collapsed, rubble everywhere.
    There is a burnt-out campfire.
    There are stairs leading down.''')
    if character.hero_class == "W":
        x = convert_to_int(input('''
        Would you like to:
            1 - investigate the campfire
            2 - take the stairs down
            3 - sleep
            4 - detect magic
        '''))
        if not check_option_validity(x, [1, 2, 3, 4]):
            typing("That is not a valid option")
            upper_floor_options(character)
    elif character.hero_class == "C":
        x = convert_to_int(input('''
        Would you like to:
            1 - investigate the campfire
            2 - take the stairs down
            3 - sleep
            5 - heal
        '''))
        if not check_option_validity(x, [1, 2, 3, 5]):
            typing("That is not a valid option")
            upper_floor_options(character)
    else:
        x = convert_to_int(input('''
        Would you like to:
            1 - investigate the campfire
            2 - take the stairs down
            3 - sleep
        '''))
        if not check_option_validity(x, [1, 2, 3]):
            typing("That is not a valid option")
            upper_floor_options(character)

    if x == 1:
        investigate_the_campfire(character)
    if x == 2:
        tower_lower_floor.introduction(character)
    if x == 3:
        actions.sleep(character, 'outside')
        upper_floor_options(character)
    if x == 4:
        detect_magic_on_the_tower_upper_floor(character)
    if x == 5:
        actions.heal(character)
        upper_floor_options(character)


def investigate_the_campfire(character):
    fire = "The campfire on the tower's upper floor"
    typing("The campfire looks to be about a week old")
    if 'flint and steel' in character.equipment:
        actions.light_fire(character, fire)


def detect_magic_on_the_tower_upper_floor(character):
    typing("There is no magic here. You will continue detecting magic for a while")
    upper_floor_options(character)
