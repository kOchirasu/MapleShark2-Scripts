from script_api import *

f = AddByte("Function")

if f == 0:
    count = AddShort("Count")
    for i in range(count):
        AddInt("StampId")
    count = AddShort("Count")
    for i in range(count):
        AddInt("Unknown")
        AddInt("-1")
        AddInt("217538647")
