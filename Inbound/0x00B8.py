from script_api import *

f = AddByte("function")

if f == 22: # load
    AddInt("Unknown")
    AddInt("Score")
    AddInt("HighestScore")
    AddInt("Unknown")
elif f == 23: # pvp stats
    count = AddInt("count")
    for i in range(count):
        with Node("Stats " + str(i), True):
            AddInt("JobCode")
            AddInt("Wins")
            AddInt("Losses")
