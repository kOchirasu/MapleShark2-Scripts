from script_api import *

f = AddByte("Function")
b = AddBool("Unknown")

count = AddInt("count")
for i in range(count):
    with Node("Entry " + str(i)):
        AddInt("a")
        AddInt("a")
        AddUnicodeString("a")
        AddLong("Timestamp")
