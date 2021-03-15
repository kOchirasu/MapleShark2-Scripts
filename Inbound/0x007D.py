from script_api import *
from common import *

f = AddByte("function")
if f == 0: # load
    AddInt("ObjectId")
    AddLong("DollUid")
    AddInt("DollItemId")
    DecodeCoordF("Position")
    DecodeCoordF("Rotation")
    AddBool("HasITems")
    count = AddInt("count")
    for i in range(count):
        with Node("Item " + str(i)):
            id = AddInt("ItemId")
            AddLong("ItemUid")
            AddUnicodeString("slot")
            AddInt("rarity")
            DecodeItem(id)
elif f == 1: # remove
    AddInt("ObjectId")
elif f == 6: # put item on doll
    AddLong("DollUid")
    id = AddInt("ItemId")
    AddLong("ItemUid")
    AddUnicodeString("slot")
    AddInt("rarity")
    DecodeItem(id)
elif f == 7: # remove item
    AddLong("ItemUid")
    AddUnicodeString("Slot")
elif f == 8:
    # Feature 233 locked
    AddLong("Unknown")
    AddInt("Unknown") # n - 23
elif f == 11:
    AddInt("ErrorCode")
