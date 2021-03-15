from script_api import *

f = AddByte("Function")

if f == 0: # deposit
    AddLong("Unknown")
    AddLong("itemUid")
    AddShort("Slot")
    AddInt("amount")
elif f == 1: # withdraw
    AddLong("Unknown")
    AddLong("ItemUid")
    AddShort("slot")
    AddInt("amount")
elif f == 2: # move item
    AddLong("Unknown")
    AddLong("uid")
    AddShort("dstSlot")
elif f == 3: # update mesos (start loading after 13)
    AddLong("Unknown")
    AddBool("deposit")
    AddLong("Mesos")
elif f == 4: # start loading after 3
    AddLong("Unknown") # 0
    AddShort("MaxSlots")
elif f == 6: # Expand slots
    AddLong("Unknown") # 0
elif f == 8: # sort update
    AddLong("Unknown")
