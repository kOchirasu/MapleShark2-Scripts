from script_api import *
from common import *

f = AddByte("Function")

if f == 0: # add
    AddLong("Unknown")
    # some condition
    id = AddInt("itemId")
    AddLong("itemUid")
    AddShort("Slot")
    AddInt("rarity")
    DecodeItem(id)
elif f == 1: # remove all
    AddLong("Unknown")
    AddLong("ItemUid")
elif f == 2: # move item
    AddLong("Unknown")
    AddLong("uid")
    AddShort("srcSlot")
    AddLong("uid")
    AddShort("dstSlot")
elif f == 3: # update mesos (start loading after 13)
    AddLong("Mesos") # 0
elif f == 4: # start loading after 3
    AddLong("Unknown") # 0
    AddShort("MaxSlots")
elif f == 5: # load items after 4
    AddLong("Unknown")
    count = AddShort("Count")
    for i in range(count):
        with Node("Item " + str(i)):
            id = AddInt("itemId")
            AddLong("itemUid")
            AddShort("Slot")
            AddInt("rarity")
            DecodeItem(id)
elif f == 7 or f == 8: # sort update
    AddLong("Unknown")
    count = AddShort("Count")
    for i in range(count):
        with Node("Item " + str(i)):
            id = AddInt("itemId")
            AddLong("itemUid")
            AddShort("Slot")
            AddInt("rarity")
            DecodeItem(id)
elif f == 9: # remove some
    AddLong("Unknown")
    # some condition
    AddLong("ItemUid")
    AddInt("remaining")
elif f == 11: # reset, response to 0x0C also sent before sort update
    pass # none
elif f == 13: # Start loading after 11
    AddInt("Unknown") # 0
elif f == 14 or f == 16:
    pass
