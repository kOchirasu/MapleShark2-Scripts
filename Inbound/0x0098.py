from script_api import *

f = AddByte("function")

if f == 1: # confirm put item
    AddLong("ItemUid")
    AddShort("slot")
    AddInt("Amount")
elif f == 2: # confirm remove item
    AddLong("ItemUid")
elif f == 3: # dismantle results
    AddByte("Unknown")
    count = AddInt("count")
    for i in range(count):
        with Node("Item " + str(i), True):
            AddInt("ItemId")
            AddInt("Amount")
elif f == 5: # preview dismantle results
    count = AddInt("count")
    for i in range(count):
        with Node("Item " + str(i), True):
            AddInt("ItemId")
            AddInt("amount min")
            AddInt("amount max")
