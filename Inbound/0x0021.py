from script_api import *
from common import *

f = AddByte("function")
if f == 13: # Start inventory?
    AddInt("???")
elif f == 0:
    with Node("Item"):
        id = AddInt("ItemId")
        AddLong("uid")
        AddShort("slot")
        AddInt("rarity")
        AddUnicodeString("???")
        DecodeItem(id)
elif f == 8:
    AddLong("ItemUid")
    AddInt("Amount")
    AddUnicodeString("Unknown")
    # more...
elif f == 7 or f == 10:
    count = AddShort("count")
    for i in range(count):
        with Node("Item " + str(i)):
            id = AddInt("ItemId")
            AddLong("uid")
            AddShort("slot")
            AddInt("rarity")
            DecodeItem(id)
elif f == 1: # Remove all
    AddLong("ItemUid")
elif f == 2: # Updates amount of item in inventory
    AddLong("ItemUid")
    AddInt("Amount")
elif f == 3: # Move item
    AddLong("uid")
    AddShort("srcSlot")
    AddLong("uid")
    AddShort("dstSlot")
elif f == 14:
    pass
