from script_api import *

def AddBuddyEntry():
    with Node("Entry"):
        AddLong("EntryUid")
        AddLong("CharacterId")
        AddLong("AccountId")
        AddUnicodeString("Name")
        AddUnicodeString("RequestMessage")
        AddShort("Unknown")
        AddInt("MapId")
        AddInt("JobCode")
        AddInt("JobId")
        AddShort("Level")
        with Node("Flags"):
            for i in range(5):
                AddBool("Flag-bit " + str(i))
        
        AddLong("Timestamp")
        AddUnicodeString("ProfileUrl")
        AddUnicodeString("Motto")
        AddUnicodeString("Unknown")
        AddInt("Unknown")
        AddInt("Unknown")
        AddInt("Unknown")
        AddUnicodeString("HouseName")
        AddLong("Unknown")
        with Node("Trophy"):
            for i in range(3):
                AddInt("Count")


# Me
# 2755522640508123531
# 2754959794319858342

# 2740889794779415829
# 2755801783803708036
# 2759038746032736787

# 2759038746032736787
# 2755801783803708036
f = AddByte("function")
if f == 1: # load
    count = AddInt("count")
    for i in range(count):
        AddBuddyEntry()
elif f == 2: # Request friend
    AddByte("Unknown")
    AddUnicodeString("Name")
elif f == 3: # and 7
    AddByte("Unknown") # 0
    AddLong("EntryUid")
    AddLong("CharacterId")
    AddLong("AccountId")
    AddUnicodeString("Name")
elif f == 4: # and 6 (unblock 1) and 17
    AddByte("Unknown") # 0
    AddLong("EntryUid")
elif f == 5 or f == 7: # Remove Entry (unblocking, cancelling request)
    AddByte("Unknown")
    AddLong("EntryUid")
    AddLong("CharacterId")
    AddLong("AccountId")
    AddUnicodeString("Name")
elif f == 8: # Also use to update buddy map/online
    AddBuddyEntry()
elif f == 9: # Add Entry (blocking, request friend)
    AddBuddyEntry()
elif f == 10: # update block reason
    AddByte("Unknown") # 0
    AddLong("EntryUid") # uid of the block entry
    AddUnicodeString("Name")
    AddUnicodeString("BlockMsg")
    AddByte("Unknown") # 0
    AddLong("EntryUid") # uid of the block entry
    AddUnicodeString("Name")
elif f == 11 or f == 12: # block 1
    AddByte("Unknown")
    AddUnicodeString("Name")
elif f == 14:
    AddByte("Unknown")
    AddLong("EntryUid")
    AddUnicodeString("Name")
elif f == 15: # Reset (Start load)
    pass # None
elif f == 17: # cancel friend request
    AddByte("Unknown")
    AddLong("EntryUid")
elif f == 19:
    AddInt("FriendCount")
