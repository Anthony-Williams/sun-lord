from functions import typing, convert_to_int, wandering_encounter_outside_result, wandering_encounter_inside_result, you_died


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


def fight(character, wandering_encounter):
    # todo
    you_died()


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