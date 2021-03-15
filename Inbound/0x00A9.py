from script_api import *

f = AddByte("Function")
if f == 0:
    for i in range(8):
        AddShort("Unknown")
elif f == 1:
    count = AddShort("Count")
    for i in range(count):
        AddShort("Unknown")
