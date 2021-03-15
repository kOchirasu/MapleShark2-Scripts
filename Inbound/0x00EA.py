from script_api import *

f = AddByte("function")
if f == 0:
    AddUnicodeString("Unknown")
    AddInt("Unknown")
elif f == 1:
    AddInt("NpcObjectId")
    AddUnicodeString("Unknown")
elif f == 2:
    AddInt("NpcObjectId")
    AddUnicodeString("Unknown")
elif f == 3:
    AddByte("Unknown")
    AddInt("duration")
    AddString("Unknown")
    AddString("illust")
    AddString("sound")
    AddString("Unknown")
    AddUnicodeString("message")
