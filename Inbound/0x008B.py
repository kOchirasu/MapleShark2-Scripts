from script_api import *

count = AddInt("count")
for i in range(count):
    with Node("Entry " + str(i)):
        AddInt("Unknown")
        AddInt("Unknown")

AddByte("Unknown")
