from dungeon import tower_lower_floor
from dungeon import tower_hidden_floor
from functions import typing, convert_to_int, check_option_validity
from actions import noncombat


def introduction(character, world):
    typing('''The roof has collapsed, rubble everywhere.
    There is a burnt-out campfire.
    There are stairs leading down.''')
    upper_floor_options(character, world)


def upper_floor_options(character, world):
    if character.hero_class == "W":
        x = convert_to_int(input(typing('''As you stand there, your wizard senses tingle.
        There is magic here.
        You focus your senses, and can detect illusion magic above you.
        Would you like to:
            1 - investigate the campfire
            2 - take the stairs down
            3 - sleep
            5 - dispel the illusion
        ''')))
        if not check_option_validity(x, [1, 2, 3, 5]):
            typing("That is not a valid option")
            upper_floor_options(character, world)
    elif character.hero_class == "C":
        x = convert_to_int(input(typing('''
        Would you like to:
            1 - investigate the campfire
            2 - take the stairs down
            3 - sleep
            4 - heal
        ''')))
        if not check_option_validity(x, [1, 2, 3, 4]):
            typing("That is not a valid option")
            upper_floor_options(character, world)
    else:
        x = convert_to_int(input(typing('''
        Would you like to:
            1 - investigate the campfire
            2 - take the stairs down
            3 - sleep
        ''')))
        if not check_option_validity(x, [1, 2, 3]):
            typing("That is not a valid option")
            upper_floor_options(character, world)

    if x == 1:
        investigate_the_campfire(character, world)
    if x == 2:
        tower_lower_floor.introduction(character, world)
    if x == 3:
        actions.sleep(character, world, 'outside')
        upper_floor_options(character, world)
    if x == 4:
        actions.heal(character)
        upper_floor_options(character, world)
    if x == 5:
        tower_hidden_floor.introduction(character, world)


def investigate_the_campfire(character, world):
    fire = 'tower_upper_floor'
    if world.get_tower_upper_floor_campfire() == 'old':
        typing("The campfire looks to be about a week old")
    if 'flint and steel' in character.equipment:
        actions.light_fire(character, world, fire)
    upper_floor_options(character, world)
