from script_api import *

f = AddByte("function")

if f == 1: # equip
    AddInt("EquipSlot")
    AddLong("ItemUid")
elif f == 2: # unequip
    AddInt("EquipSlot")
elif f == 3: # stage upgrade
    AddLong("ItemUid") # 0 while equipped
    AddInt("ItemId")
    AddInt("EquipSlot")
elif f == 4: # stage upgrade catalysts
    AddLong("TargetItemUid") # 0 while equipped
    AddInt("TargetItemId")
    AddInt("TargetEquipSlot")
    AddInt("CatalystAmount")
elif f == 5: # upgrade (Target is the lapenshard being upgraded)
    AddLong("TargetItemUid") # 0 while equipped
    AddInt("TargetItemId")
    AddInt("TargetEquipSlot")
    count = AddInt("count")
    for i in range(count):
        with Node("catalyst", True):
            AddLong("CatalystItemUid")
            AddInt("CatalystAmount")
elif f == 6:
    AddInt("Unknown")
