''' ITEM_SOCKET_SCROLL '''
from script_api import *
from item import *

f = add_byte("function")
if f == 0:
    add_long("itemUid")
    add_int("SuccessRate")
    add_byte("SocketCount")
elif f == 2: # s_itemsocket_scroll_complete_use
    add_bool("Success")
    add_long("itemUid")
    add_byte("unknown")
    add_int("SuccessRate")
    decode_gem_sockets()
elif f == 3:
    add_byte("unknown")
    message = add_int("message")
    if message == 1:
        pass # s_itemsocket_scroll_error_invalid_target
    elif message == 2:
        pass # s_itemsocket_scroll_error_invalid_scroll
    elif message == 3:
        pass # s_itemsocket_scroll_error_invalid_disable
    elif message == 4:
        pass # s_itemsocket_scroll_error_socket_unlock_all
    elif message == 5:
        pass # s_itemsocket_scroll_error_impossible_slot
    elif message == 6:
        pass # s_itemsocket_scroll_error_impossible_rank
    elif message == 7:
        pass # s_itemsocket_scroll_error_impossible_level
    elif message == 8:
        pass # s_itemsocket_scroll_error_impossible_usepart
    elif message == 9:
        pass # s_itemsocket_scroll_error_server_fail_consume_scroll
    elif message == 10:
        pass # s_itemsocket_scroll_error_server_fail_unlock_socket
    elif message == 11:
        pass # s_itemsocket_scroll_error_already_socket_unlock
    else:
        pass # s_itemsocket_scroll_error_server_default