from script_api import *

f = AddByte("Function")

if f == 0:
    count = AddShort("count")
    for i in range(count):
        with Node("Entry " + str(i)):
            AddInt("Index+1000")
            AddInt("QuestId?") # Some id
            AddLong("Timestamp") # Intervals of 5min (spawn time?)
