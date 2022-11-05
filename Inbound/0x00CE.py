''' PET '''
from script_api import *
from item import *


def decode_field_pet():
    b = add_bool("Bool")
    if b:
        id = add_int("PetItemId")
        add_long("PetUid")
        add_int("Rarity")
        decode_item(id)
        # add_long("PetUid")

def decode_pet_profile():
    with Node("PetProfile", True):
        add_unicode_str("Name")
        add_long("Exp")
        add_int("unknown")
        add_short("Level")
        add_short("unknown (1)")
        add_short("unknown (1)")

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
    decode_field_pet()
elif f == 1: # Remove
    # BROADCAST
    add_int("PlayerObjectId")
    add_long("PetUid")
elif f == 2: # sound related
    add_int("PlayerObjectId")
elif f == 4: # Rename
    add_int("PlayerObjectId")
    decode_pet_profile()
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
elif f == 8: # add collection
    add_int("PetId")
    add_short("PetRarity")
elif f == 9: # load pet info
    add_int("PlayerObjectId")
    decode_pet_profile()
    decode_potion_settings()
    decode_loot_settings()
elif f == 10: # fusion
    add_int("PlayerObjectId")
    add_long("Exp")
    add_long("PetUid")
elif f == 11: # Level up
    add_int("PlayerObjectId")
    add_int("level")
    add_long("PetUid")
elif f == 12: # UIPetSystemDialog
    add_int("FusionCount")
elif f == 15:
    add_bool("IsSummoned")
elif f == 16: # inspecting another player's pet
    add_int("PlayerObjectId")
    id = add_int("ItemId")
    add_long("ItemUid")
    add_int("Rarity")
    decode_item(id)
elif f == 17: # evolve
    add_int("PlayerObjectId")
    add_long("ItemUid")
    add_byte("Rarity")
    add_int("Amount")
    decode_item(PET_ID)
elif f == 18: # evolve points
    add_int("PlayerObjectId")
    add_int("Points")
    add_long("ItemUid")
elif f == 19:
    message = add_int("message")
    if message == 27:
        pass # s_err_lack_meso
    elif message == 28:
        pass # s_err_lack_merat_ask
    elif message == 30:
        pass # s_item_err_store_full
    elif message == 32:
        pass # s_pet_extension_period_limit
    elif message == 33:
        pass # s_pet_error_summon_potion
    elif message == 39:
        pass # None
    else:
        pass # s_common_error_unknown
elif f == 20: # use master snare
    add_int("ItemId") # Lapis master snare
elif f == 21:
    add_int("PlayerObjectId")
    decode_field_pet()
