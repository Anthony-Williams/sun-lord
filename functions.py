import random
from random import randint
import os
import sys
from time import sleep

from hero_class import Hero


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


def create_character():
    hero_array, hero_class, hero_name = create_hero()
    character = Hero(max_health=hero_array[0], health=hero_array[1], max_melee=hero_array[2],
                     melee=hero_array[3], ranged=hero_array[4], stealth=hero_array[5],
                     defence=hero_array[6], max_magic=hero_array[7], magic=hero_array[8],
                     gold=hero_array[9], hero_class=hero_class, name=hero_name,
                     equipment=['fishing rod'])
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


def take_damage(character, damage):
    character.set_health(character.get_health() - damage)
    if character.get_health() <= 0:
        you_died()


def you_died():
    typing("You are dead")
    sleep(3)
    exit()


def check_option_validity(x, options):
    return x in options


def wandering_encounter_outside():
    # todo
    x = randint(1, 6) + randint(1, 6) + randint(1, 6)
    outside_encounters = ['troll', 'sheep', 'giant toad'] * 6
    return outside_encounters[x]
