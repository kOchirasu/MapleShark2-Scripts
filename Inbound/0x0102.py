from script_api import *

f = add_byte("Function")

if f == 0: # available missions
    add_int("count")
    add_int("DungeonId")
elif f == 1: # finish dungeon mission
    add_int("count") # ?
    # Dungeon mission class
    add_int("DungeonId")
    add_short("")
    add_short("")
elif f == 2: # mission results
    count = add_int("Count")
    for i in range(count):
        pass
elif f == 3: # finish dungeon
    add_bool("Unknown") # 1
