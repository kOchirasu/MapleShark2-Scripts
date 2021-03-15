from script_api import *

f = AddByte("function")
if f == 1:
    count = 1
else:
    count = AddInt("count")

for i in range(count):
    with Node("Breakable " + str(i), True):
        AddString("EntityId")
        AddByte("Unknown") # 2
        AddByte("Visible?") # 1
        AddInt("Unknown")
        AddInt("ServerTick")
