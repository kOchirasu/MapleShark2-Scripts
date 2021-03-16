from script_api import *

f = add_byte("function")

if f == 1: # equip
    add_int("EquipSlot")
    add_long("ItemUid")
elif f == 2: # unequip
    add_int("EquipSlot")
elif f == 3: # stage upgrade
    add_long("ItemUid") # 0 while equipped
    add_int("ItemId")
    add_int("EquipSlot")
elif f == 4: # stage upgrade catalysts
    add_long("TargetItemUid") # 0 while equipped
    add_int("TargetItemId")
    add_int("TargetEquipSlot")
    add_int("CatalystAmount")
elif f == 5: # upgrade (Target is the lapenshard being upgraded)
    add_long("TargetItemUid") # 0 while equipped
    add_int("TargetItemId")
    add_int("TargetEquipSlot")
    count = add_int("count")
    for i in range(count):
        with Node("catalyst", True):
            add_long("CatalystItemUid")
            add_int("CatalystAmount")
elif f == 6:
    add_int("Unknown")
