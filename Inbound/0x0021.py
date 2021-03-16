from script_api import *
from common import *

f = add_byte("function")
if f == 13: # Start inventory?
    add_int("???")
elif f == 0:
    with Node("Item"):
        id = add_int("ItemId")
        add_long("uid")
        add_short("slot")
        add_int("rarity")
        add_unicode_str("???")
        decode_item(id)
elif f == 8:
    add_long("ItemUid")
    add_int("Amount")
    add_unicode_str("Unknown")
    # more...
elif f == 7 or f == 10:
    count = add_short("count")
    for i in range(count):
        with Node("Item " + str(i)):
            id = add_int("ItemId")
            add_long("uid")
            add_short("slot")
            add_int("rarity")
            decode_item(id)
elif f == 1: # Remove all
    add_long("ItemUid")
elif f == 2: # Updates amount of item in inventory
    add_long("ItemUid")
    add_int("Amount")
elif f == 3: # Move item
    add_long("uid")
    add_short("srcSlot")
    add_long("uid")
    add_short("dstSlot")
elif f == 14:
    pass
