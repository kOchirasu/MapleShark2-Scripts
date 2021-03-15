from script_api import *

f = AddByte("function")
if f == 0:
    count = AddInt("Count")
    for i in range(count):
        AddLong("Unknown")
        AddInt("BanType?")
        AddLong("AccountId")
        AddUnicodeString("BlockReason")
        AddLong("StartDate")
        AddLong("EndDatei")
