from functions import typing, convert_to_int, check_option_validity

from actions import combat

def list(character, wandering_encounter):
    typing(f"The {wandering_encounter.get_name()} has:")
    for x in range(0, len(wandering_encounter.get_loot())):
        typing(f"- {wandering_encounter.get_loot()[x]}")
    y = convert_to_int(input(typing("Which item would you like to loot?")))
    if y > len(wandering_encounter.get_loot()):
        typing("That is not a valid option")
        list(character, wandering_encounter)
    else:
        typing(f"You loot the {wandering_encounter.get_loot()[y-1]}")
        loot_effects(character, wandering_encounter.get_loot()[y-1])
        wandering_encounter.set_negative_loot(wandering_encounter.get_loot()[y-1])
        combat.fight_victory(character, wandering_encounter)

def loot_effects(character, loot):
    if loot == "troll blood":
        troll_blood(character)

def troll_blood(character):
    x = convert_to_int(input(typing('''
    Would you like to:
        1 - drink the troll blood
        2 - pocket it
    ''')))
    if not check_option_validity(x, [1, 2]):
        typing("That is not a valid option")
        troll_blood(character)
    if x == 1:
        character.set_health(character.get_health() + 2)
    if x == 2:
        character.set_positive_equipment("troll blood")