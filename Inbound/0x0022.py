from script_api import *
from common import *

f = add_byte("Function")

if f == 0: # add
    add_long("Unknown")
    # some condition
    id = add_int("itemId")
    add_long("itemUid")
    add_short("Slot")
    add_int("rarity")
    decode_item(id)
elif f == 1: # remove all
    add_long("Unknown")
    add_long("ItemUid")
elif f == 2: # move item
    add_long("Unknown")
    add_long("uid")
    add_short("srcSlot")
    add_long("uid")
    add_short("dstSlot")
elif f == 3: # update mesos (start loading after 13)
    add_long("Mesos") # 0
elif f == 4: # start loading after 3
    add_long("Unknown") # 0
    add_short("MaxSlots")
elif f == 5: # load items after 4
    add_long("Unknown")
    count = add_short("Count")
    for i in range(count):
        with Node("Item " + str(i)):
            id = add_int("itemId")
            add_long("itemUid")
            add_short("Slot")
            add_int("rarity")
            decode_item(id)
elif f == 7 or f == 8: # sort update
    add_long("Unknown")
    count = add_short("Count")
    for i in range(count):
        with Node("Item " + str(i)):
            id = add_int("itemId")
            add_long("itemUid")
            add_short("Slot")
            add_int("rarity")
            decode_item(id)
elif f == 9: # remove some
    add_long("Unknown")
    # some condition
    add_long("ItemUid")
    add_int("remaining")
elif f == 11: # reset, response to 0x0C also sent before sort update
    pass # none
elif f == 13: # Start loading after 11
    add_int("Unknown") # 0
elif f == 14 or f == 16:
    pass
