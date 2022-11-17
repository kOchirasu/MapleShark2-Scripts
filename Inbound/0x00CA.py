''' CHANGE_ATTRIBUTES '''
from script_api import *
from item import *

f = add_byte("function")
if f == 1:
    add_long("ItemUid")
    decode_item(0)
elif f == 2:
    add_long("ItemUid")
    decode_item(0)
elif f == 4:
    b = add_bool("flag") # m_remakeOptionIngredient, m_itemBag
    message = add_int("message")
    if message == 1:
        pass # s_itemremake_error_server_not_in_inven
    elif message == 2:
        pass # s_itemremake_error_server_impossible
    elif message == 3 or message == 4:
        pass # s_itemremake_error_server_null_status
    elif message == 5:
        pass # s_itemremake_error_server_lack_price
    elif message == 6 or message == 7:
        pass # s_itemremake_error_server_fail_apply_option
    elif message == 9:
        pass # s_itemremake_error_server_fail_lack_lock_consume_item
    elif message == 10:
        pass # s_content_shutdown_notice
    else:
        pass # s_itemremake_error_server_default
