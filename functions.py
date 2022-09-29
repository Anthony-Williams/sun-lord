import random
from random import randint
import os
import sys
from time import sleep

from world import World
from hero_class import Hero
from monster import Monster


def clear_screen():
    sleep(2)
    os.system('cls')


# function for making the illusion of typing on every print
def typing(message):
    # todo uncomment
    print(message)
    return ""
#    print("")
#    for word in message:
#        sleep(random.choice([0.3, 0.11, 0.08, 0.07, 0.07, 0.07, 0.06, 0.06, 0.05, 0.01]))
#        sys.stdout.write(word)
#        sys.stdout.flush()
#    sleep(.1)
#    return ""


def convert_to_int(string):
    try:
        return int(string)
    except ValueError:
        return convert_to_int(input("Please input an integer\n"))


def create_world():
    return World(weather=None, time_unit=10, magic_time_marker=-1, tower_upper_floor_campfire="old", purple_moss=True)

def create_character():
    hero_array, hero_class, hero_name = create_hero()
    character = Hero(max_health=hero_array[0], health=hero_array[1], max_melee=hero_array[2],
                     melee=hero_array[3], ranged=hero_array[4], stealth=hero_array[5],
                     defence=hero_array[6], max_magic=hero_array[7], magic=hero_array[8],
                     gold=hero_array[9], hero_class=hero_class, name=hero_name,
                     equipment=[])
    return character


def create_hero():
    global max_health, health, max_melee, melee, ranged, stealth, defence, max_magic, magic, gold, hero_class, hero_array
    x = convert_to_int(input(typing("Choose your class:\n1 - cleric\n2 - fighter\n3 - thief\n4 - wizard\n")))
    while x not in [1, 2, 3, 4]:
        typing("Please input an integer 1-4")
        x = convert_to_int(input(typing("Choose your class:\n1 - cleric\n2 - fighter\n3 - thief\n4 - wizard\n")))

    hero_points = 8
    if x == 1:
        hero_array = create_cleric(hero_points)
        hero_class = "C"
    if x == 2:
        hero_array = create_fighter(hero_points)
        hero_class = "F"
    if x == 3:
        hero_array = create_thief(hero_points)
        hero_class = "T"
    if x == 4:
        hero_array = create_wizard(hero_points)
        hero_class = "W"

    sleep(1)
    hero_name = input(typing("And now, brave hero, what is your name?\n"))
    typing(f"You have created your character, {hero_name}...")

    return hero_array, hero_class, hero_name


def create_cleric(hero_points):
    typing("You have chosen cleric!")
    typing(f"You have {hero_points} points to put into melee, defence, and magic")
    max_health = 10
    health = max_health
    hero_points, max_melee = input_hero_points(hero_points, "melee")
    melee = max_melee
    ranged = 0
    stealth = 0
    hero_points, defence = input_hero_points(hero_points, "defence")
    hero_points, max_magic = input_hero_points(hero_points, "magic")
    magic = max_magic
    gold = random.randint(1, 6)
    return [max_health, health, max_melee, melee, ranged, stealth, defence, max_magic, magic, gold]


def create_fighter(hero_points):
    typing("You have chosen fighter!")
    typing(f"You have {hero_points} points to put into melee, ranged, and defence\n")
    max_health = 12
    health = max_health
    hero_points, max_melee = input_hero_points(hero_points, "melee")
    melee = max_melee
    hero_points, ranged = input_hero_points(hero_points, "ranged")
    stealth = 0
    hero_points, defence = input_hero_points(hero_points, "defence")
    max_magic = 0
    magic = max_magic
    gold = random.randint(1, 12)
    return [max_health, health, max_melee, melee, ranged, stealth, defence, max_magic, magic, gold]


def create_thief(hero_points):
    typing("You have chosen thief!")
    typing(f"You have {hero_points} points to put into ranged, and stealth\n")
    max_health = 8
    health = max_health
    max_melee = 0
    melee = max_melee
    hero_points, ranged = input_hero_points(hero_points, "ranged")
    hero_points, stealth = input_hero_points(hero_points, "stealth")
    defence = 0
    max_magic = 0
    magic = max_magic
    gold = random.randint(6, 12)
    return [max_health, health, max_melee, melee, ranged, stealth, defence, max_magic, magic, gold]


def create_wizard(hero_points):
    typing("You have chosen wizard!")
    typing(f"All of your {hero_points} points are put into magic")
    max_health = 6
    health = max_health
    max_melee = 0
    melee = max_melee
    ranged = 0
    stealth = 0
    defence = 0
    max_magic = hero_points
    magic = max_magic
    gold = random.randint(1, 8)
    return [max_health, health, max_melee, melee, ranged, stealth, defence, max_magic, magic, gold]


def input_hero_points(hero_points, stat):
    input_stat = convert_to_int(input(typing(f"How many of your {hero_points} points would you like in {stat}?\n")))
    if input_stat > hero_points:
        typing(f"You only have {hero_points} points.")
        input_hero_points(hero_points, stat)
    else:
        hero_points -= input_stat
        typing(f"You have put {input_stat} into {stat} and have {hero_points} remaining")
    return hero_points, input_stat


def equip(character):
    equipment = character.get_equipment()
    if 'dagger' in equipment:
        character.set_max_melee(character.get_max_melee() + 1)
        character.set_melee(character.get_melee() + 1)
    if 'sword' in equipment:
        character.set_max_melee(character.get_max_melee() + 2)
        character.set_melee(character.get_melee() + 2)
    if 'longbow' in equipment:
        character.set_ranged(character.get_ranged() + 1)
    if 'shield' in equipment:
        character.set_defence(character.get_defence() + 2)
    if 'cloak of stealth' in equipment:
        character.set_stealth(character.get_stealth() + 3)


def you_died():
    typing("You are dead")
    sleep(3)
    exit()


def check_option_validity(x, options):
    return x in options


def wandering_encounter_outside_result():
    # todo
    x = randint(1, 6) + randint(1, 6) + randint(1, 6) - 1
    troll = Monster("troll", 16, 6, "slow", 4, 0, ["troll blood", "big club", "sheep skull"])
    sheep = Monster("sheep", 4, 0, "normal", 2, 0, ["sheep meat"])
    giant_toad = Monster("giant toad", 6, 3, "fast", 4, 0, ["gems in the stomach"])
    outside_encounter = [
                            troll,
                            sheep,
                            giant_toad
                        ] * 6
    return outside_encounter[x]
def wandering_encounter_inside_result():
    # todo
    inside_encounter = ['spider', 'fly']
    return random.choice(inside_encounter)