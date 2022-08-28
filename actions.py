import random
from random import randint

from functions import typing, convert_to_int, wandering_encounter_outside_result, wandering_encounter_inside_result, \
    you_died, check_option_validity


def light_fire(character, world, fire):
    if fire == 'tower_upper_floor':
        world.set_tower_upper_floor_campfire(True)
        fire_descriptor = "The campfire on the tower's upper floor"
    typing(f"{fire_descriptor} is lit, crackling merrily")


def heal(character):
    x = convert_to_int(input(typing(f"You have {character.get_magic()} healing spells available. \
    Each heals for two health. How many would you like to use?\n")))
    if x > character.get_magic():
        typing("That is more healing than you have available.")
        heal(character)
    else:
        character.set_health(character.get_health() + (x*2))
        typing(f"You have healed for {x*2} health")


def sleep(character, world, location):
    hours = convert_to_int(input(typing("How many hours would you like to sleep for?\n")))
    for x in range(0, hours):
        if location == 'outside':
            sleep_one_hour_outside(character, world)


def sleep_one_hour_outside(character, world):
    # todo detail dangerous monsters
    dangerous_outside_monsters = ['troll']
    wandering_encounter = wandering_encounter_outside_result()
    if wandering_encounter in dangerous_outside_monsters:
        typing(f"Your sleep is interrupted by a {wandering_encounter}")
        encounter(character, wandering_encounter)
    else:
        if 'bedroll' in character.equipment:
            character.set_health(character.get_health() + 3)
        else:
            character.set_health(character.get_health()+2)
        world.set_new_weather()
        typing(f"You wake up refreshed. The weather is {world.get_weather()}")


def fight_start_options(character, wandering_encounter):
    typing(f"The {wandering_encounter} will be on you in a few seconds.")
    if character.get_ranged > 0:
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
    elif character.get_magic > 0:
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



def fight_melee(character, wandering_encounter):
    # todo
    return


def run(character, wandering_encounter):
    speed = wandering_encounter.get_speed
    if speed == 'slow' or (speed == 'normal' and random.random() < .5):
        typing(f"You escape from the {wandering_encounter}.")
        return
    else:
        typing(f"The {wandering_encounter} catches up to you.")
        fight_melee(character, wandering_encounter)


def hide(character, wandering_encounter):
    if randint(1,20)+character.get_stealth > randint(1,20):
        typing(f"The {wandering_encounter} passes by you.")
        return
    else:
        typing(f"The {wandering_encounter} has noticed you.")
        fight_melee(character, wandering_encounter)


def fight_ranged(character, wandering_encounter):
    # todo
    return


def fight_magic(character, wandering_encounter):
    typing(f"You have {character.get_magic} magic points remaining.")
    spells = ['sleep', 'web', 'fireball', 'lightning bolt']
    spells_available = spells[:character.get_magic]
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


def take_damage(character, damage):
    character.set_health(character.get_health() - damage)
    if character.get_health() <= 0:
        you_died()
    if character.get_max_health()/2 > character.get_health():
        typing("You have taken a lot of damage, perhaps sleep or heal yourself?")

def time_count(character, world, location):
    world.set_time_unit(world.get_time_unit()-1)
    if world.get_magic_time_marker() == world.get_time_unit():
        character.set_detecting_magic(False)
    if world.get_time_unit() == 0:
        world.set_time_unit(10)
        if location == 'outside':
            monster = wandering_encounter_outside_result()
        else:
            monster = wandering_encounter_inside_result()
        encounter(character, monster)


def encounter(character, monster):
    you_died()