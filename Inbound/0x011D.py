from script_api import *

f = AddByte("function")

if f == 0: # load
    count = AddInt("count")
    for i in range(count):
        with Node("Lapenshard " + str(i), True):
            AddInt("EquipSlot")
            AddInt("ItemId")
elif f == 1: # equip
    AddInt("EquipSlot")
    AddInt("ItemId")
elif f == 2: # unequip
    AddInt("EquipSlot")
elif f == 4: # lapenshard stage update
    AddInt("SuccessRate") # 10000 = 100%
elif f == 5: # lapenshard upgraded
    # if upgrading equipped, send 0x00
    AddLong("TargetItemUid") # 0
    AddInt("TargetItemId") # oldId
    AddInt("Unknown") #0
    AddBool("Success")
