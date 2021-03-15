from script_api import *

f = AddByte("Function")
if f == 22:
    AddInt("Unknown")
    AddInt("Unknown")
    AddLong("Unknown")
    AddUnicodeString("UnknownStr")
    AddInt("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
elif f == 23:
    AddLong("Unknown")
    AddInt("Unknown")
    AddByte("Unknown")
    AddLong("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
    AddLong("Unknown")
elif f == 30:
    count = AddByte("Count")
    for i in range(count):
        AddInt("Unknown")
        count2 = AddInt("Count")
        for j in range(count2):
            AddInt("Unknown")
            AddLong("Unknown")
