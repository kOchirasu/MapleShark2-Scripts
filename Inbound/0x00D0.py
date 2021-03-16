from script_api import *
from common import *

f = add_byte("Function")

if f == 0: # Store item
    id = add_int("Id")
    add_long("Uid")
    add_short("Slot")
    add_int("Rarity")
    add_unicode_str("UnknownStr")
    decode_item(id)
elif f == 1: # Remove item
    add_long("ItemUid")
elif f == 2: # Update amount
    add_long("ItemUid")
    add_int("Amount")
elif f == 3: # move item
    add_long("SrcItemUid")
    add_short("SrcSlot")
    add_long("DstItemUid")
    add_short("DstSlot")
elif f == 4:
    count = add_short("Count")
    for i in range(count):
        with Node("Item " + str(i)):
            id = add_int("Id")
            add_long("Uid")
            add_short("Slot")
            add_int("Rarity")
            decode_item(id)
elif f == 6: # Start item inventory list
    pass
