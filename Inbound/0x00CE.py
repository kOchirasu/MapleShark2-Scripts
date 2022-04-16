from script_api import *
from item import *

def decode_potion_settings():
    with Node("PotionSettings", True):
        count = add_byte("Count")
        for i in range(count):
            with Node("Potion " + str(i), True):
                add_int("ThresholdIndex")
                add_float("Threshold")
                add_int("ItemId")

def decode_loot_settings():
    with Node("LootSettings", True):
        add_bool("Mesos")
        add_bool("Merets")
        add_bool("Other")
        add_bool("Currency")
        add_bool("Equipment")
        add_bool("Consumable")
        add_bool("Gemstone")
        add_bool("Dropped")
        add_int("MinRarity")
        add_bool("Enabled")


f = add_byte("Function")
if f == 0: # Add
    # BROADCAST
    add_int("PlayerObjectId")
    add_int("PetObjectId")
    b = add_bool("Bool")
    if b:
        id = add_int("PetItemId")
        add_long("PetUid")
        add_int("Rarity")
        decode_item(id)
        add_long("PetUid")
elif f == 1: # Remove
    # BROADCAST
    add_int("PlayerObjectId")
    add_long("PetUid")
elif f == 5:
    add_int("PlayerObjectId")
    decode_potion_settings()
elif f == 6:
    add_int("PlayerObjectId")
    decode_loot_settings()
elif f == 7: # load collection
    count = add_int("Count")
    for i in range(count):
        add_int("PetId")
        add_short("PetRarity")
elif f == 9:
    add_int("PlayerObjectId")
    add_unicode_str("PetName")
    add_long("PetExp")
    add_int("Unknown")
    add_short("Unknown")
    add_short("Unknown")
    add_short("Unknown")
    decode_potion_settings()
    decode_loot_settings()
elif f == 20: # use master snare
    add_int("ItemId") # Lapis master snare
