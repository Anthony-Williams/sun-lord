from random import randint

from functions import typing, you_died


def purple_moss(character):
    if character.get_health() <= 10:
        if randint(1, 20) < 10:
            typing('''You smell a sweet, sugary smell, drowsiness filling your mind, overcoming your senses.
                   The soporific effect overpowers your ability to shake it off.
                   You fall to the floor, asleep.''')
            you_died()
        else:
            typing('''You smell a sweet, sugary smell, drowsiness filling your mind.
                   You shake off the soporific effect.''')
    else:
        typing("You smell a sweet, sugary smell.")
