from functions import typing, convert_to_int, wandering_encounter_outside


def light_fire(character, fire):
    typing(f"{fire} is lit")


def heal(character):
    x = convert_to_int(input(typing(f"You have {character.get_magic()} healing spells available. \
    Each heals for two health. How many would you like to use?\n")))
    if x > character.get_magic():
        typing("That is more healing than you have available.")
        heal(character)
    else:
        character.set_health(character.get_health() + (x*2))
        typing(f"You have healed for {x*2} health")


def sleep(character, location):
    hours = convert_to_int(input(typing("How many hours would you like to sleep for?\n")))
    for x in range(0, hours):
        if location == 'outside':
            sleep_one_hour_outside(character)


def sleep_one_hour_outside(character):
    # todo
    dangerous_outside_monsters = ['troll']
    wandering_encounter = wandering_encounter_outside()
    if wandering_encounter in dangerous_outside_monsters:
        typing(f"Your sleep is interrupted by a {wandering_encounter}")
        fight(character, wandering_encounter)
    else:
        character.set_health(character.get_health()+2)


def fight(character, wandering_encounter):
    # todo
    typing("You die!")
