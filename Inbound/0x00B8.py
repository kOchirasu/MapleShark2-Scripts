from script_api import *

f = add_byte("function")

if f == 22: # load
    add_int("Unknown")
    add_int("Score")
    add_int("HighestScore")
    add_int("Unknown")
elif f == 23: # pvp stats
    count = add_int("count")
    for i in range(count):
        with Node("Stats " + str(i), True):
            add_int("JobCode")
            add_int("Wins")
            add_int("Losses")
