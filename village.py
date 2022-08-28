import pandas as pd
import re
from functions import typing, check_option_validity, convert_to_int


def introduction(character):
    village_name = 'Scunthorpe'
    typing(f"Welcome to the humble village of {village_name}, {character.get_name()}")
    wares = [['dagger', '+1 melee', 1],
             ['flint and steel', 'can light fires', 1],
             ['fishing rod', 'can fish', 1],
             ['sword', '+2 melee', 2],
             ['longbow', '+1 ranged', 2],
             ['shield', '+2 defence', 2],
             ['cloak of stealth', '+2 stealth', 3],
             ['nothing', 'leave the shop', 0]
             ]
    shopping(character, wares)
    typing(f"Goodbye, {character.get_name()}, and safe travels!")


def shopping(character, wares):
    typing(f"You have {character.get_gold()} gold to spend")
    typing("The shopkeeper offers to sell you:")
    wares_title = ['Item', 'Description', 'Cost']
    df = pd.DataFrame(wares, columns = wares_title, index=[x for x in range(1, len(wares)+1)])
    typing(df)
    purchase = convert_to_int(input())
    if not check_option_validity(purchase, [x for x in range(1, len(wares)+1)]):
        typing("That is not a valid option")
        shopping(character, wares)
    if wares[purchase-1][0] == "nothing":
        return
    if wares[purchase-1][2] > character.get_gold():
        typing(f"You cannot afford that, {character.get_name()}")
        shopping(character, wares)
    else:
        character.set_positive_equipment(re.sub(" +", " ", wares[purchase-1][0]))
        character.set_gold(character.get_gold()-wares[purchase-1][2])
        wares.pop(purchase-1)
        shopping(character, wares)
