from script_api import *
from common import *

def DecodePotionSettings():
    with Node("PotionSettings", True):
        count = AddByte("Count")
        for i in range(count):
            with Node("Potion " + str(i), True):
                AddInt("ThresholdIndex")
                AddFloat("Threshold")
                AddInt("ItemId")

def DecodeLootSettings():
    with Node("LootSettings", True):
        AddBool("Mesos")
        AddBool("Merets")
        AddBool("Other")
        AddBool("Currency")
        AddBool("Equipment")
        AddBool("Consumable")
        AddBool("Gemstone")
        AddBool("Dropped")
        AddInt("MinRarity")
        AddBool("Enabled")


f = AddByte("Function")
if f == 0: # Add
    # BROADCAST
    AddInt("PlayerObjectId")
    AddInt("PetObjectId")
    b = AddBool("Bool")
    if b:
        id = AddInt("PetItemId")
        AddLong("PetUid")
        AddInt("Rarity")
        DecodeItem(id)
        AddLong("PetUid")
elif f == 1: # Remove
    # BROADCAST
    AddInt("PlayerObjectId")
    AddLong("PetUid")
elif f == 5:
    AddInt("PlayerObjectId")
    DecodePotionSettings()
elif f == 6:
    AddInt("PlayerObjectId")
    DecodeLootSettings()
elif f == 7: # load collection
    count = AddInt("Count")
    for i in range(count):
        AddInt("PetId")
        AddShort("PetRarity")
elif f == 9:
    AddInt("PlayerObjectId")
    AddUnicodeString("PetName")
    AddLong("PetExp")
    AddInt("Unknown")
    AddShort("Unknown")
    AddShort("Unknown")
    AddShort("Unknown")
    DecodePotionSettings()
    DecodeLootSettings()
elif f == 20: # use master snare
    AddInt("ItemId") # Lapis master snare
