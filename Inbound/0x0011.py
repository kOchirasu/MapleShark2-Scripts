from script_api import *

f = AddByte("function")
if f == 0:
    AddInt("ServerTick")
    AddLong("Timestamp")
    AddByte("Unknown")
    AddInt("Unknown")
    AddInt("Key")
elif f == 1:
    AddInt("ServerTick")
    AddLong("Timestamp")
    AddByte("Unknown")
    AddInt("Unknown")
elif f == 2:
    AddInt("ServerTick")
    AddLong("Timestamp")
    AddByte("Unknown")
    AddInt("Unknown")
elif f == 3:
    AddLong("Timestamp")
