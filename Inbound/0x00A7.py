from script_api import *

f = AddByte("function")
if f == 0:
    pass
elif f == 1:
    AddInt("Unknown")
elif f == 2:
    AddInt("Unknown")
elif f == 3:
    AddByte("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
"""for i in range(15):
    with Node("Entry " + str(i), True):
        AddInt("Id")
        AddInt("Level")
        AddInt("Unknown")
        AddShort("Unknown")
        AddField("Unknown", 38)
"""
