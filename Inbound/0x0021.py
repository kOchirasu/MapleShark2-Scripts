''' ITEM_INVENTORY '''
from script_api import *
from item import *

f = add_byte("function")
if f == 0:
    with Node("Item"):
        id = add_int("ItemId")
        add_long("uid")
        add_short("slot")
        add_int("rarity")
        add_unicode_str("SlotType")
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
elif f == 8:
    add_long("ItemUid")
    add_int("Amount")
    add_unicode_str("SlotType")
    # more...
elif f == 7:
    count = add_short("count")
    for i in range(count):
        with Node("Item " + str(i)):
            id = add_int("ItemId")
            add_long("uid")
            add_short("slot")
            add_int("rarity")
            decode_item(id)
elif f == 10: # sub_C4FDD0
    count = add_short("count")
    for i in range(count):
        with Node("Item " + str(i)):
            id = add_int("ItemId")
            add_long("uid")
            add_short("slot")
            add_int("rarity")
            decode_item(id)
if f == 13: # Start inventory?
    add_int("???")
elif f == 14:
    # Feature_129_BagRenewal01
    add_byte("unknown")
    add_int("unknown")
    pass
elif f == 15: # Error
    message = add_int("message")
    '''
    if message == 12:
        pass # s_item_err_invalid_count
    elif message == 13:
        pass # s_err_inventory
    elif message == 31:
        pass # s_err_cannot_destroy_petitem_hasitem
    elif message == 34:
        pass # related to case 14
    elif message == 35:
        pass # s_item_err_puton_invalid_binding
    elif message == 36:
        pass # s_item_err_use_invalid_binding
    elif message == 37:
        pass # s_item_err_Invalid_slot_codi
    elif message == 38:
        pass # s_item_err_not_active_tab
    elif message == 40:
        pass # s_itemdrop_error_restricted_by_user_level_ex
    elif message == 41:
        pass # s_itempickup_error_restricted_by_user_level_ex
    elif message == 42:
        pass # s_item_err_drop
    else:
        pass # s_item_err_code
    '''
elif f == 16:
    add_long("uid")