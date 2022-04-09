''' STORAGE_INVENTORY '''
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
elif f == 7: # storage dialog expand?
    pass
elif f == 8: # sort update
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
elif f == 14: # open dialog?
    pass
elif f == 16: # error
    message = add_int("message")
    '''
    if message == 10:
        pass # s_item_err_invalid_count
    elif message == 12:
        pass # s_item_err_invaild_store_type
    elif message == 13:
        pass # s_item_err_store_full
    elif message == 14:
        pass # s_store_err_expand_max
    elif message == 15:
        pass # s_cannot_charge_merat
    elif message == 16:
        pass # s_item_err_binditem
    elif message == 17:
        pass # s_item_err_binditem_store_out
    elif message == 18:
        pass # s_store_err_deposit_disable_type
    elif message == 19:
        pass # s_store_err_deposit_invalid_money
    elif message == 20:
        pass # s_store_err_deposit_max_money
    elif message == 21:
        pass # s_cashshop_lack_balance
    elif message == 22:
        pass # s_item_err_moveDisableitem_store_out
    else:
        pass # s_store_err_code
    '''
