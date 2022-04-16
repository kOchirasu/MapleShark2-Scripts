from script_api import *
from item import *

f = add_byte("Function")
if f == 5:
    # Start enchanting?
    enchantType = add_short("EnchantType") # 1 = Ophelia, 2 = Peachy
    # Some condition or else: stop here
    add_long("ItemUid")
    count = add_byte("RequiredItemCount")
    for i in range(count):
        with Node("RequiredItem"):
            add_int("Unknown")
            add_int("RequiredItem (DiffId)") # 100 = crytal frag, 101 = onyx, 102 = chaos
            add_int("Amount")
        
    add_short("Unknown")

    count = add_int("Count")
    for i in range(count):
        decode_stat_option(i)

    if enchantType == 1:
        add_float("SuccessRate") # 100
        add_float("Unknown")
        add_float("Unknown")
        add_float("Unknown")
        add_float("Unknown")
        add_long("Unknown")
        add_long("Unknown")
        add_byte("Unknown")
    # Required item copies
    if enchantType == 1 or enchantType == 2:
        add_int("ItemId")
        add_short("Rarity")
        add_int("Amount")
elif f == 6: # This is sent with peachy
    add_long("ItemUid")
    add_int("Unknown") # progress related for peachy?
elif f == 7:
    add_int("Unknown")
    add_int("Unknown")
    count = add_int("Count")
    for i in range(count):
        add_long("Unknown")
    add_float("Unknown")
    add_float("Unknown")
    add_float("Unknown")
    add_float("Unknown")
    add_float("Unknown")
elif f == 8:
    add_int("Unknown")
    count = add_int("Count")
    for i in range(count):
        add_long("Unknown")
elif f == 9:
    pass # Some AAErr
elif f == 10:
    add_long("ItemUid")
    decode_item(0) # Don't know ItemId
    # Bonus from enchanting (e.g. 2% def)
    count = add_int("Count")
    for i in range(count):
        decode_stat_option(i)
elif f == 11:
    add_long("ItemUid")
    decode_item(0) # Don't know ItemId

    add_int("Unknown")
    add_int("Unknown")
    add_long("Unknown")
    add_int("Unknown")
elif f == 12:
    add_short("Unknown")
elif f == 15:
    add_long("ItemUid")
