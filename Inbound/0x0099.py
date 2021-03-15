from script_api import *
from common import *

f = AddByte("Function")
if f == 5:
    # Start enchanting?
    enchantType = AddShort("EnchantType") # 1 = Ophelia, 2 = Peachy
    # Some condition or else: stop here
    AddLong("ItemUid")
    count = AddByte("RequiredItemCount")
    for i in range(count):
        with Node("RequiredItem"):
            AddInt("Unknown")
            AddInt("RequiredItem (DiffId)") # 100 = crytal frag, 101 = onyx, 102 = chaos
            AddInt("Amount")
        
    AddShort("Unknown")

    count = AddInt("Count")
    for i in range(count):
        DecodeStatOption(i)

    if enchantType == 1:
        AddFloat("SuccessRate") # 100
        AddFloat("Unknown")
        AddFloat("Unknown")
        AddFloat("Unknown")
        AddFloat("Unknown")
        AddLong("Unknown")
        AddLong("Unknown")
        AddByte("Unknown")
    # Required item copies
    if enchantType == 1 or enchantType == 2:
        AddInt("ItemId")
        AddShort("Rarity")
        AddInt("Amount")
elif f == 6: # This is sent with peachy
    AddLong("ItemUid")
    AddInt("Unknown") # progress related for peachy?
elif f == 7:
    AddInt("Unknown")
    AddInt("Unknown")
    count = AddInt("Count")
    for i in range(count):
        AddLong("Unknown")
    AddFloat("Unknown")
    AddFloat("Unknown")
    AddFloat("Unknown")
    AddFloat("Unknown")
    AddFloat("Unknown")
elif f == 8:
    AddInt("Unknown")
    count = AddInt("Count")
    for i in range(count):
        AddLong("Unknown")
elif f == 9:
    pass # Some AAErr
elif f == 10:
    AddLong("ItemUid")
    DecodeItem(0) # Don't know ItemId
    # Bonus from enchanting (e.g. 2% def)
    count = AddInt("Count")
    for i in range(count):
        DecodeStatOption(i)
elif f == 11:
    AddLong("ItemUid")
    DecodeItem(0) # Don't know ItemId

    AddInt("Unknown")
    AddInt("Unknown")
    AddLong("Unknown")
    AddInt("Unknown")
elif f == 12:
    AddShort("Unknown")
elif f == 15:
    AddLong("ItemUid")
