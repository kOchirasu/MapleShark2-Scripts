from script_api import *

f = AddByte("function")
if f == 0:
    AddByte("Unknown")
    AddInt("ServerTick")
    AddInt("Duration (ms)")
    AddInt("Unknown")
elif f == 1:
    AddInt("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
elif f == 2:
    AddByte("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
elif f == 3:
    pass # none
elif f == 4:
    pass # none
elif f == 5:
    pass # none
