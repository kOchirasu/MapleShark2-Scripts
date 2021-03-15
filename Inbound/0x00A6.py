from script_api import *

f = AddByte("function")

if f == 6:
    count = AddInt("count")
    for i in range(count):
        AddInt("Id")
        AddLong("Timestamp")
