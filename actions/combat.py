import random
from random import randint

from actions import noncombat, loot
from functions import typing, convert_to_int, wandering_encounter_outside_result, wandering_encounter_inside_result, \
    you_died, check_option_validity

def fight_start_options(character, wandering_encounter):
    typing(f"Suddenly, a {wandering_encounter.get_name()} approaches! It will be on you in a few seconds.")
    if character.get_ranged() > 0:
        x = convert_to_int(input(typing('''
        Would you like to 
            1 - melee fight
            2 - run
            3 - hide
            4 - ranged fight
        ''')))
        if not check_option_validity(x, [1, 2, 3, 4]):
            typing("That is not a valid option")
            fight_start_options(character, wandering_encounter)
    elif character.get_magic() > 0 and character.get_hero_class() == "C":
        x = convert_to_int(input(typing('''
        Would you like to 
            1 - melee fight
            2 - run
            3 - hide
            5 - magic fight
        ''')))
        if not check_option_validity(x, [1, 2, 3, 5]):
            typing("That is not a valid option")
            fight_start_options(character, wandering_encounter)
    elif character.get_hero_class() == "W":
        if character.get_magic() > 0:
            x = convert_to_int(input(typing('''
                    Would you like to 
                        2 - run
                        3 - hide
                        5 - magic fight
                    ''')))
            if not check_option_validity(x, [2, 3, 5]):
                typing("That is not a valid option")
                fight_start_options(character, wandering_encounter)
        else:
            x = convert_to_int(input(typing('''
                                Would you like to 
                                    2 - run
                                    3 - hide
                                ''')))
            if not check_option_validity(x, [2, 3]):
                typing("That is not a valid option")
                fight_start_options(character, wandering_encounter)
    else:
        x = convert_to_int(input(typing('''
        Would you like to 
            1 - melee fight
            2 - run
            3 - hide
        ''')))
        if not check_option_validity(x, [1, 2, 3]):
            typing("That is not a valid option")
            fight_start_options(character, wandering_encounter)

    if x==1:
        fight_melee(character, wandering_encounter)
    if x==2:
        run(character, wandering_encounter)
    if x==3:
        hide(character, wandering_encounter)
    if x==4:
        fight_ranged(character, wandering_encounter)
    if x==5:
        fight_magic(character, wandering_encounter)

def fight_continue_options(character, wandering_encounter):
    typing(f"You are fighting {wandering_encounter.get_name()}.")
    x = convert_to_int(input(typing('''
    Would you like to 
        1 - melee fight
        2 - run
        3 - hide
    ''')))
    if not check_option_validity(x, [1, 2, 3]):
        typing("That is not a valid option")
        fight_continue_options(character, wandering_encounter)
    if x==1:
        fight_melee(character, wandering_encounter)
    if x==2:
        run(character, wandering_encounter)
    if x==3:
        hide(character, wandering_encounter)

def fight_melee(character, wandering_encounter):
    # todo
    if character.get_hero_class() == "T" or wandering_encounter.get_speed() == "slow":
        character_attack(character, wandering_encounter)
        if wandering_encounter.get_health() <= 0:
            typing(f"You killed {wandering_encounter.get_name()}!")
            fight_victory(character, wandering_encounter)
            return
        monster_attack(character, wandering_encounter)
    else:
        monster_attack(character, wandering_encounter)
        character_attack(character, wandering_encounter)
        if wandering_encounter.get_health() <= 0:
            typing(f"You killed {wandering_encounter.get_name()}!")
            fight_victory(character, wandering_encounter)
            return
    fight_continue_options(character, wandering_encounter)

def character_attack(character, wandering_encounter):
    damage = character.get_melee() - wandering_encounter.get_defence()
    if damage > 0:
        typing(f"You swing at the {wandering_encounter.get_name()}, dealing {damage} damage.")
        wandering_encounter.set_health(wandering_encounter.get_health() - damage)
    else:
        typing(f"The {wandering_encounter.get_name()}'s defence is too good, you deal no damage.")

def monster_attack(character, wandering_encounter):
    damage = wandering_encounter.get_melee() - character.get_defence()
    if damage > 0:
        typing(f"The {wandering_encounter.get_name()} swings at you, dealing {damage} damage.")
        noncombat.take_damage(character, damage)
    else:
        typing(f"Your defence is too good, the {wandering_encounter.get_name()} deals no damage.")

def run(character, wandering_encounter):
    speed = wandering_encounter.get_speed()
    if speed == 'slow' or (speed == 'normal' and random.random() < .5):
        typing(f"You escape from the {wandering_encounter.get_name()}.")
        return
    else:
        typing(f"The {wandering_encounter.get_name()} catches up to you.")
        fight_melee(character, wandering_encounter)


def hide(character, wandering_encounter):
    if randint(1,20)+character.get_stealth() > randint(1,20):
        typing(f"The {wandering_encounter.get_name()} passes by you.")
        return
    else:
        typing(f"The {wandering_encounter.get_name()} has noticed you.")
        fight_melee(character, wandering_encounter)


def fight_ranged(character, wandering_encounter):
    # todo
    return


def fight_magic(character, wandering_encounter):
    typing(f"You have {character.get_magic()} magic points remaining.")
    spells = ['sleep', 'web', 'fireball', 'lightning bolt']
    spells_available = spells[:character.get_magic()]
    typing("Would you like to cast")
    for i in range(0, len(spells_available)):
        typing(f"\t{i+1} - {spells_available[i]}")
    x = convert_to_int(input())
    if not check_option_validity(x, [range(1, len(spells_available)+1)]):
        typing("That is not a valid option")
        fight_magic(character, wandering_encounter)
    cast_spell(character, wandering_encounter, spells[x])


def cast_spell(character, wandering_encounter, spell):
    # todo
    return

def fight_victory(character, wandering_encounter):
    typing(f'''Congratulations on defeating {wandering_encounter.get_name()}.
It has {wandering_encounter.get_gold()} gold and {len(wandering_encounter.get_loot())} pieces of loot.''')
    if wandering_encounter.get_gold() > 0 and len(wandering_encounter.get_loot()) > 0:
        x = convert_to_int(input(typing(f'''
            Would you like to:
                1 - leave the corpse
                2 - take the gold
                3 - loot
            ''')))
        if not check_option_validity(x, [1, 2, 3]):
            typing("That is not a valid option")
            fight_victory(character, wandering_encounter)
    elif wandering_encounter.get_gold() > 0:
        x = convert_to_int(input(typing(f'''
            Would you like to:
                1 - leave the corpse
                2 - take the gold
            ''')))
        if not check_option_validity(x, [1, 2]):
            typing("That is not a valid option")
            fight_victory(character, wandering_encounter)
    elif len(wandering_encounter.get_loot()) > 0:
        x = convert_to_int(input(typing(f'''
            Would you like to:
                1 - leave the corpse
                3 - loot
            ''')))
        if not check_option_validity(x, [1, 3]):
            typing("That is not a valid option")
            fight_victory(character, wandering_encounter)
    else:
        x = convert_to_int(input(typing(f'''
                Would you like to:
                    1 - leave the corpse
                ''')))
        if not check_option_validity(x, [1]):
            typing("That is not a valid option")
            fight_victory(character, wandering_encounter)

    if x == 1:
        return
    if x == 2:
        character.set_gold(character.get_gold() + wandering_encounter.get_gold())
        wandering_encounter.set_gold(0)
        fight_victory(character, wandering_encounter)
    if x == 3:
        loot.list(character, wandering_encounter)