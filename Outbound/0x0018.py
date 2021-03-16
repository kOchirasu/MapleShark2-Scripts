from script_api import *

f = add_byte("Function")

if f == 0: # deposit
    add_long("Unknown")
    add_long("itemUid")
    add_short("Slot")
    add_int("amount")
elif f == 1: # withdraw
    add_long("Unknown")
    add_long("ItemUid")
    add_short("slot")
    add_int("amount")
elif f == 2: # move item
    add_long("Unknown")
    add_long("uid")
    add_short("dstSlot")
elif f == 3: # update mesos (start loading after 13)
    add_long("Unknown")
    add_bool("deposit")
    add_long("Mesos")
elif f == 4: # start loading after 3
    add_long("Unknown") # 0
    add_short("MaxSlots")
elif f == 6: # Expand slots
    add_long("Unknown") # 0
elif f == 8: # sort update
    add_long("Unknown")
