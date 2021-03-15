from script_api import *

f = AddByte("function")
if f == 0:
    AddLong("ItemUid")
    AddField("Unknown", 8)
    b = AddBool("UseLock")
    if b:
        AddByte("Unknown")
        AddShort("LockedIndex")
elif f == 2: # Select new option
    AddLong("ItemUid")
