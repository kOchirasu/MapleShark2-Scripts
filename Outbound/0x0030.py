from script_api import *

f = AddByte("function")

if f == 2: # request
    AddUnicodeString("Name")
    AddUnicodeString("Message")
elif f == 3: # accept
    AddLong("EntryUid")
elif f == 4: # decline
    AddLong("EntryUid")
elif f == 5: # block
    AddLong("EntryUid")
    AddUnicodeString("Name")
    AddUnicodeString("BlockReason")
elif f == 6: # unblock
    AddLong("EntryUid")
elif f == 7: # remove friend
    AddLong("EntryUid")
elif f == 10: # update block msg
    AddLong("EntryUid")
    AddUnicodeString("Name")
    AddUnicodeString("BlockReason")
elif f == 17: # cancel friend request
    AddLong("EntryUid")
