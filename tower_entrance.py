from random import randint

import tower_lower_floor
import tower_upper_floor
from functions import typing, convert_to_int, check_option_validity, wandering_encounter_outside, take_damage


def introduction(character):
    typing("Greetings, brave adventurer!")
    typing('''A minor local noble recently went missing, and you have been contracted to try and find him.
    Your map has taken you on a three-day trek through an infested swamp, fighting off overgrown toads and 
    blood-sucking bat-mosquito spawn, whilst dancing lights tried to tempt you off your path. You stand 
    outside the tumble-down remnants of an ancient tower, the ruins that the noble supposedly went to 
    investigate. 
    A few small fish dart around your feet, the stagnant water lapping at your boots. The tower looms 
    before you, its entrance-way awaiting you, hungrily.''')
    tower_options(character)


def tower_options(character):
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
            tower_options(character)
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
            tower_options(character)
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
            tower_options(character)
    else:
        x = convert_to_int(input('''Would you like to
            1 - go inside
            2 - look inside
            3 - climb the tower
            4 - circle the tower
            '''))
        if not check_option_validity(x, [1, 2, 3, 4]):
            typing("That is not a valid option")
            tower_options(character)
    if x == 1:
        go_inside_the_tower(character)
    if x == 2:
        look_inside_the_tower(character)
    if x == 3:
        climb_the_tower(character)
    if x == 4:
        circle_the_tower(character)
    if x == 5:
        go_fishing_by_the_tower(character)
    if x == 6:
        detect_magic_by_the_tower(character)


def go_inside_the_tower(character):
    tower_lower_floor.introduction(character)


def look_inside_the_tower(character):
    # todo
    return ""


def climb_the_tower(character):
    x = randint(1, 20)
    if character.hero_class == "T":
        x += 5
    if x < 8:
        take_damage(character, randint(1, 6))
        typing("You slip and fall, injuring yourself")
        tower_options(character)
    else:
        typing("You climb up to the second floor of the tower")
        tower_upper_floor.upper_floor_options(character)


def circle_the_tower(character):
    x = randint(1, 20)
    if character.hero_class == "T":
        x += 5

    if 5 > x:
        typing("You find nothing")
        tower_options(character)
    elif 10 > x > 5:
        typing(f"You find tracks from a {wandering_encounter_outside()}")
    elif 15 > x > 10:
        typing(f"You find tracks from a {wandering_encounter_outside()} and a {wandering_encounter_outside()}")
    elif 20 > x > 15:
        typing(f"You find tracks from a {wandering_encounter_outside()} and a {wandering_encounter_outside()} and a {wandering_encounter_outside()}")
    else:
        typing(f"You find tracks from a {wandering_encounter_outside()} and a {wandering_encounter_outside()} and a {wandering_encounter_outside()} and a {wandering_encounter_outside()}")
    tower_options(character)


def go_fishing_by_the_tower(character):
    fish = randint(1, 4)
    typing(f"You fish for ten minutes and catch {fish} fish")
    for x in range(1, fish):
        character.equipment.append('fish')
    tower_options(character)


def detect_magic_by_the_tower(character):
    typing("There is no magic here. You will continue detecting magic for a while")
    tower_options(character)
