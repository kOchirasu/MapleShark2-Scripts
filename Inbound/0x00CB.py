''' CHANGE_ATTRIBUTES_SCROLL '''
from script_api import *
from item import *

f = add_byte("Function")
if f == 0: # use scroll response
    add_long("ScrollUid")
elif f == 2: # use scroll on item
    add_long("EquipUid")
    decode_item(0)
    # s_itemremake_scroll_error_have_not_item
elif f == 3: # select new item
    add_long("EquipUid")
    decode_item(0)
elif f == 4: # error
    add_bool("unknown")
    message = add_int("message")
    if message == 1:
        pass # s_itemremake_scroll_error_invalid_target
    elif message == 2:
        pass # s_itemremake_scroll_error_invalid_target_data
    elif message == 3:
        pass # s_itemremake_scroll_error_invalid_target_stat
    elif message == 4:
        pass # s_itemremake_scroll_error_impossible_slot
    elif message == 5:
        pass # s_itemremake_scroll_error_impossible_rank
    elif message == 6:
        pass # s_itemremake_scroll_error_impossible_level
    elif message == 7:
        pass # s_itemremake_scroll_error_impossible_property
    elif message == 8:
        pass # s_itemremake_scroll_error_impossible_item
    elif message == 10:
        pass # s_itemremake_scroll_error_invalid_scroll
    elif message == 11:
        pass # s_itemremake_scroll_error_invalid_scroll_data
    elif message == 12 or message == 13:
        pass # s_itemremake_scroll_error_server_fail_remake
    elif message == 14:
        pass # s_itemremake_scroll_error_server_fail_apply_before_option
    elif message == 15:
        pass # s_itemremake_scroll_error_server_fail_consume_scroll
    elif message == 16:
        pass # s_itemremake_error_server_fail_lack_lock_consume_item
    elif message == 17:
        pass # s_content_shutdown_notice
    else:
        pass # s_itemremake_scroll_error_server_default
