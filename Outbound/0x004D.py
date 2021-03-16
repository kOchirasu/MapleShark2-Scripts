from script_api import *

f = add_byte("function")
if f == 1: # create group
    add_unicode_str("Unknown")
elif f == 2: # invite player
    add_unicode_str("UserName")
    add_int("GroupChatId")
elif f == 4: # leave group
    add_int("GroupChatId")
    add_bool("Unknown") # 0
elif f == 10: # message group
    add_unicode_str("Message")
    add_int("GroupChatId")
