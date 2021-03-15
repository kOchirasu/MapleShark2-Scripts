from script_api import *
from common import *

f = AddByte("Function")

if f == 0: # Store item
    id = AddInt("Id")
    AddLong("Uid")
    AddShort("Slot")
    AddInt("Rarity")
    AddUnicodeString("UnknownStr")
    DecodeItem(id)
elif f == 1: # Remove item
    AddLong("ItemUid")
elif f == 2: # Update amount
    AddLong("ItemUid")
    AddInt("Amount")
elif f == 3: # move item
    AddLong("SrcItemUid")
    AddShort("SrcSlot")
    AddLong("DstItemUid")
    AddShort("DstSlot")
elif f == 4:
    count = AddShort("Count")
    for i in range(count):
        with Node("Item " + str(i)):
            id = AddInt("Id")
            AddLong("Uid")
            AddShort("Slot")
            AddInt("Rarity")
            DecodeItem(id)
elif f == 6: # Start item inventory list
    pass
