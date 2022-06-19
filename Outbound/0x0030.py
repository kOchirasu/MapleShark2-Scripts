from script_api import *

f = add_byte("function")

if f == 2: # request
    add_unicode_str("Name")
    add_unicode_str("Message")
elif f == 3: # accept
    add_long("EntryUid")
elif f == 4: # decline
    add_long("EntryUid")
elif f == 5: # block
    add_long("EntryUid")
    add_unicode_str("Name")
    add_unicode_str("BlockReason")
elif f == 6: # unblock
    add_long("EntryUid")
elif f == 7: # remove friend
    add_long("EntryUid")
elif f == 10: # update block msg
    add_long("EntryUid")
    add_unicode_str("Name")
    add_unicode_str("BlockReason")
elif f == 17: # cancel friend request
    add_long("EntryUid")
elif f == 20:
    add_int("unknown") # bool? (CGameOptionPtr+284 != 0)