from script_api import *

def add_buddyEntry():
    with Node("Entry"):
        add_long("EntryUid")
        add_long("CharacterId")
        add_long("AccountId")
        add_unicode_str("Name")
        add_unicode_str("RequestMessage")
        add_short("Unknown")
        add_int("MapId")
        add_int("JobCode")
        add_int("JobId")
        add_short("Level")
        with Node("Flags"):
            for i in range(5):
                add_bool("Flag-bit " + str(i))
        
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


# Me
# 2755522640508123531
# 2754959794319858342

# 2740889794779415829
# 2755801783803708036
# 2759038746032736787

# 2759038746032736787
# 2755801783803708036
f = add_byte("function")
if f == 1: # load
    count = add_int("count")
    for i in range(count):
        add_buddyEntry()
elif f == 2: # Request friend
    add_byte("Unknown")
    add_unicode_str("Name")
elif f == 3: # and 7
    add_byte("Unknown") # 0
    add_long("EntryUid")
    add_long("CharacterId")
    add_long("AccountId")
    add_unicode_str("Name")
elif f == 4: # and 6 (unblock 1) and 17
    add_byte("Unknown") # 0
    add_long("EntryUid")
elif f == 5 or f == 7: # Remove Entry (unblocking, cancelling request)
    add_byte("Unknown")
    add_long("EntryUid")
    add_long("CharacterId")
    add_long("AccountId")
    add_unicode_str("Name")
elif f == 8: # Also use to update buddy map/online
    add_buddyEntry()
elif f == 9: # Add Entry (blocking, request friend)
    add_buddyEntry()
elif f == 10: # update block reason
    add_byte("Unknown") # 0
    add_long("EntryUid") # uid of the block entry
    add_unicode_str("Name")
    add_unicode_str("BlockMsg")
    add_byte("Unknown") # 0
    add_long("EntryUid") # uid of the block entry
    add_unicode_str("Name")
elif f == 11 or f == 12: # block 1
    add_byte("Unknown")
    add_unicode_str("Name")
elif f == 14:
    add_byte("Unknown")
    add_long("EntryUid")
    add_unicode_str("Name")
elif f == 15: # Reset (Start load)
    pass # None
elif f == 17: # cancel friend request
    add_byte("Unknown")
    add_long("EntryUid")
elif f == 19:
    add_int("FriendCount")
