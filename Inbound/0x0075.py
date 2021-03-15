from script_api import *

f = AddByte("Function")

if f == 0:
    count = AddInt("count")
    for i in range(count):
        with Node("Liftable " + str(i), True):
            AddString("Unknown")
            AddByte("Unknown")
            AddInt("Unknown")
            AddByte("Unknown")
            AddUnicodeString("Unknown")
            AddUnicodeString("Unknown")
            AddUnicodeString("Unknown")
            AddUnicodeString("Unknown")
            AddBool("Unknown")
elif f == 2:
    AddString("Unknown")
    AddByte("Unknown")
    AddInt("Unknown")
    AddByte("Unknown")
elif f == 3:
    AddString("Unknown")
    AddInt("Unknown")
    AddUnicodeString("Unknown")
    AddUnicodeString("Unknown")
    AddUnicodeString("Unknown")
    AddUnicodeString("Unknown")
    AddBool("Unknown")
elif f == 4:
    AddString("Unknown")
