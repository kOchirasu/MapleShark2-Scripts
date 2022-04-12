''' BUDDY '''
from script_api import *

def decode_buddy():
    with Node("Entry"):
        add_long("EntryUid")
        add_long("CharacterId")
        add_long("AccountId")
        add_unicode_str("Name")
        add_unicode_str("Message")
        add_short("Unknown")
        add_int("MapId")
        add_int("JobCode")
        add_int("JobId")
        add_short("Level")
        with Node("Flags"):
            for i in {1, 2, 3, 6, 7}:
                add_bool("Flag-bit " + str(i))
            # bit-8 is always set to 1
        
        add_long("Timestamp")
        add_unicode_str("ProfileUrl")
        add_unicode_str("Motto")
        add_unicode_str("Unknown")
        add_int("Unknown")
        add_int("Unknown")
        add_int("Unknown")
        add_unicode_str("HouseName")
        add_long("Unknown")
        with Node("Trophy"):
            for i in range(3):
                add_int("Count")

# if message == 9, also calls a function...
def buddy_error_message(message):
    '''
    if message == 1:
        pass # s_buddy_err_miss_id
    elif message == 2:
        pass # s_buddy_err_already_request_somebody
    elif message == 3:
        pass # s_buddy_err_already_buddy
    elif message == 4:
        pass # s_buddy_err_my_id_ex
    elif message == 5:
        pass # s_buddy_err_request_somebody
    elif message == 6:
        pass # s_buddy_err_max_block
    elif message == 7:
        pass # s_buddy_err_max_buddy
    elif message == 8:
        pass # s_buddy_err_target_full
    elif message == 9 or message == 11:
        pass # s_buddy_refused_request_from_somebody
    else:
        pass # s_buddy_err_unknown
    '''
    pass

# NOTE: max_length: name=12, message=25
f = add_byte("function")
if f == 1: # load
    count = add_int("count")
    for i in range(count):
        decode_buddy()
elif f == 2: # Request friend
    message = add_byte("error")
    buddy_error_message(message)
    add_unicode_str("Name")
    add_unicode_str("Message")
    # s_buddy_request_to_somebody
elif f == 3:
    add_byte("error")
    add_long("EntryUid")
    add_long("CharacterId")
    add_long("AccountId")
    add_unicode_str("Name")
    # s_buddy_add_somebody
elif f == 4:
    add_byte("error")
    add_long("EntryUid")
    # s_buddy_decline_request_from_somebody
elif f == 5: # Remove Entry
    message = add_byte("error")
    buddy_error_message(message)
    add_long("EntryUid")
    add_unicode_str("Name")
    add_unicode_str("Message")
    # s_buddy_ban_somebody
elif f == 6:
    add_byte("error")
    add_long("EntryUid")
    # s_buddy_del_somebody_from_banlist
elif f == 7:
    add_byte("error")
    add_long("EntryUid")
    add_long("CharacterId")
    add_long("AccountId")
    add_unicode_str("Name")
    # s_buddy_refused_request_from_somebody
    # s_buddy_cancel_request_from_somebody
    # s_buddy_del_somebody_from_list
elif f == 8: # Update buddy map/online
    add_byte("error")
    add_long("EntryUid")
    decode_buddy()
elif f == 9: # blocking, request friend
    add_byte("error")
    add_long("EntryUid")
    decode_buddy()
elif f == 10: # Remove Entry
    message = add_byte("error")
    buddy_error_message(message)
    add_long("EntryUid")
    add_unicode_str("Name")
    add_unicode_str("Message")
    # s_buddy_ban_memo_complete
elif f == 11: # block 1
    add_long("EntryUid") # uid of the block entry
    # s_buddy_add_somebody
elif f == 12:
    message = add_byte("error")
    buddy_error_message(message)
    add_unicode_str("Name")
    # s_buddy_err_max_block
elif f == 13:
    add_int("unknown")
    add_unicode_str("name")
    add_unicode_str("action") # "approved", "declined", "removed"
    add_long("unknown")
    # "approved" -> s_buddy_add_somebody
    # "declined" -> s_buddy_refused_request_from_somebody
    # "removed" -> s_buddy_del_somebody_from_list
elif f == 14:
    add_bool("offline")
    add_long("EntryUid")
    add_unicode_str("Name")
    # offine ? s_buddy_alert_offline_somebody : s_buddy_alert_online_somebody
elif f == 15: # Reset (Start load)
    pass # None
elif f == 17: # cancel friend request
    add_byte("error")
    add_long("EntryUid")
    # s_buddy_cancel_request
elif f == 18:
    pass # s_ban_check_err_any
elif f == 19:
    add_int("FriendCount")
elif f == 20:
    pass
# assert(f <= 20)
