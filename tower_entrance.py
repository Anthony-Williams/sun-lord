from random import randint

import actions
import tower_lower_floor
import tower_upper_floor
from functions import typing, convert_to_int, check_option_validity, wandering_encounter_outside_result


def introduction(character, world):
    typing("Greetings, brave adventurer!")
    typing('''A minor local noble recently went missing, and you have been contracted to try and find him.
    Your map has taken you on a three-day trek through an infested swamp, fighting off overgrown toads and 
    blood-sucking bat-mosquito spawn, whilst dancing lights tried to tempt you off your path. You stand 
    outside the tumble-down remnants of an ancient tower, the ruins that the noble supposedly went to 
    investigate. 
    A few small fish dart around your feet, the stagnant water lapping at your boots. The tower looms 
    before you, its entrance-way awaiting you, hungrily.''')
    typing(f"The weather is {world.get_weather()}")
    tower_options(character, world)


def tower_options(character, world):
    if character.hero_class == "W" and 'fishing rod' in character.equipment:
        x = convert_to_int(input('''Would you like to
            1 - go inside
            2 - look inside
            3 - climb the tower
            4 - circle the tower
            5 - go fishing
            6 - detect magic
            '''))
        if not check_option_validity(x, [1, 2, 3, 4, 5, 6]):
            typing("That is not a valid option")
            tower_options(character, world)
    elif character.hero_class == "W":
        x = convert_to_int(input('''Would you like to
            1 - go inside
            2 - look inside
            3 - climb the tower
            4 - circle the tower
            6 - detect magic
            '''))
        if not check_option_validity(x, [1, 2, 3, 4, 6]):
            typing("That is not a valid option")
            tower_options(character, world)
    elif 'fishing rod' in character.equipment:
        x = convert_to_int(input('''Would you like to
            1 - go inside
            2 - look inside
            3 - climb the tower
            4 - circle the tower
            5 - go fishing
            '''))
        if not check_option_validity(x, [1, 2, 3, 4, 5]):
            typing("That is not a valid option")
            tower_options(character, world)
    else:
        x = convert_to_int(input('''Would you like to
            1 - go inside
            2 - look inside
            3 - climb the tower
            4 - circle the tower
            '''))
        if not check_option_validity(x, [1, 2, 3, 4]):
            typing("That is not a valid option")
            tower_options(character, world)
    if x == 1:
        go_inside_the_tower(character, world)
    if x == 2:
        look_inside_the_tower(character, world)
    if x == 3:
        climb_the_tower(character, world)
    if x == 4:
        circle_the_tower(character, world)
    if x == 5:
        go_fishing_by_the_tower(character, world)
    if x == 6:
        detect_magic_by_the_tower(character, world)


def go_inside_the_tower(character, world):
    tower_lower_floor.introduction(character, world)


def look_inside_the_tower(character, world):
    typing('''You see a small circular room, dark and cold. 
    Stairs to your right spiral up to the upper floor.
    Stairs to your left spiral down into the earth.''')
    if world.get_purple_moss():
        typing("A large patch of purple moss grows on the far wall.")
    tower_options(character, world)


def climb_the_tower(character, world):
    x = randint(1, 20)
    if character.hero_class == "T":
        x += 5
    if x < 8:
        actions.take_damage(character, randint(1, 6))
        typing("You slip and fall, injuring yourself")
        tower_options(character, world)
    else:
        typing("You climb up to the second floor of the tower")
        tower_upper_floor.upper_floor_options(character, world)


def circle_the_tower(character, world):
    actions.time_count(character, world, 'outside')
    x = randint(1, 20)
    if character.hero_class == "T":
        x += 5

    if 5 > x:
        typing("You find nothing")
        tower_options(character, world)
    elif 10 > x > 5:
        typing(f"You find tracks from a {wandering_encounter_outside_result()}")
    elif 15 > x > 10:
        typing(f"You find tracks from a {wandering_encounter_outside_result()} and a {wandering_encounter_outside_result()}")
    elif 20 > x > 15:
        typing(f"You find tracks from a {wandering_encounter_outside_result()} and a {wandering_encounter_outside_result()} and a {wandering_encounter_outside_result()}")
    else:
        typing(f"You find tracks from a {wandering_encounter_outside_result()} and a {wandering_encounter_outside_result()} and a {wandering_encounter_outside_result()} and a {wandering_encounter_outside_result()}")
    tower_options(character, world)


def go_fishing_by_the_tower(character, world):
    actions.time_count(character, world, 'outside')
    fish = randint(1, 4)
    typing(f"You fish for ten minutes and catch {fish} fish")
    for x in range(1, fish):
        character.equipment.append('fish')
    tower_options(character, world)


def detect_magic_by_the_tower(character, world):
    actions.time_count(character, world, 'outside')
    world.set_magic_time_marker(world.get_time_unit())
    character.set_detecting_magic(True)
    typing("There is no magic here. You will continue detecting magic for a while")
    tower_options(character, world)
