from script_api import *

f = AddByte("Function")
if f == 0: # Store item
    AddLong("ItemUid")
    AddShort("Slot")
    AddInt("Amount")
elif f == 3: # Move item
    AddLong("ItemUid")
    AddShort("Slot")
elif f == 7:
    # load inventory
    pass
