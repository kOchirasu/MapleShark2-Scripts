from script_api import *

f = AddByte("Function")

if f == 0:
    count = AddInt("count")
    for i in range(count):
        AddInt("Unknown")
    AddLong("Unknown")
    AddInt("Unknown")
elif f == 1:
    AddInt("Unknown")
