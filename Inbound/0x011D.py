from script_api import *

f = add_byte("function")

if f == 0: # load
    count = add_int("count")
    for i in range(count):
        with Node("Lapenshard " + str(i), True):
            add_int("EquipSlot")
            add_int("ItemId")
elif f == 1: # equip
    add_int("EquipSlot")
    add_int("ItemId")
elif f == 2: # unequip
    add_int("EquipSlot")
elif f == 4: # lapenshard stage update
    add_int("SuccessRate") # 10000 = 100%
elif f == 5: # lapenshard upgraded
    # if upgrading equipped, send 0x00
    add_long("TargetItemUid") # 0
    add_int("TargetItemId") # oldId
    add_int("Unknown") #0
    add_bool("Success")
