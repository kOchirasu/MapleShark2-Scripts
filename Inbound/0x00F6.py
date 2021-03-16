from script_api import *

f = add_byte("Function")

if f == 0:
    count = add_short("count")
    for i in range(count):
        with Node("Entry " + str(i)):
            add_int("Index+1000")
            add_int("QuestId?") # Some id
            add_long("Timestamp") # Intervals of 5min (spawn time?)
