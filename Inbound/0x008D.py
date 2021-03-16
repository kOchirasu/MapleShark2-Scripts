from script_api import *
from common import *

f = add_byte("function")
if f == 0: # create group #1
    add_int("GroupChatId")
    count = add_byte("count")
    for i in range(count):
        t = add_byte("Type?")
        if t == 1 or t ==2:
            decode_player()
elif f == 1: # create group #2
    add_int("GroupChatId")
elif f == 2: # invite #1
    add_unicode_str("InviteSender")
    add_unicode_str("InvitedPlayer")
    add_int("GroupChatId")
elif f == 3: # receive invite
    add_unicode_str("InviteSender")
    add_unicode_str("InvitedPlayer")
    add_int("GroupChatId")
elif f == 4: # left group (self)
    add_int("GroupChatId")
elif f == 6: # invite #2
    add_int("Unknown")
    add_unicode_str("OwnerName")
    t = add_byte("Type?")
    if t == 1 or t ==2:
        decode_player()
elif f == 7: # player left group (others)
    add_int("GroupChatId")
    add_byte("Unknown")
    add_unicode_str("Name")
elif f == 8:
    add_int("GroupChatId")
    add_unicode_str("Unknown")
elif f == 9:
    add_int("GroupChatId")
    add_unicode_str("Unknown")
elif f == 10: # message group
    add_int("GroupChatId")
    add_unicode_str("UserName")
    add_unicode_str("Message")
elif f == 11:
    add_int("GroupChatId")
    add_unicode_str("Unknown")
elif f == 12:
    add_int("GroupChatId")
    add_unicode_str("Unknown")
    add_unicode_str("Unknown")
elif f == 13:
    add_byte("Unknown")
    add_int("GroupChatId")
    add_unicode_str("Unknown")
    add_unicode_str("Unknown")
