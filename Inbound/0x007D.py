from script_api import *
from item import *

f = add_byte("function")
if f == 0: # load
    add_int("ObjectId")
    add_long("DollUid")
    add_int("DollItemId")
    decode_coordF("Position")
    decode_coordF("Rotation")
    add_bool("HasITems")
    count = add_int("count")
    for i in range(count):
        with Node("Item " + str(i)):
            id = add_int("ItemId")
            add_long("ItemUid")
            add_unicode_str("slot")
            add_int("rarity")
            decode_item(id)
elif f == 1: # remove
    add_int("ObjectId")
elif f == 6: # put item on doll
    add_long("DollUid")
    id = add_int("ItemId")
    add_long("ItemUid")
    add_unicode_str("slot")
    add_int("rarity")
    decode_item(id)
elif f == 7: # remove item
    add_long("ItemUid")
    add_unicode_str("Slot")
elif f == 8:
    # Feature 233 locked
    add_long("Unknown")
    add_int("Unknown") # n - 23
elif f == 11:
    add_int("ErrorCode")
