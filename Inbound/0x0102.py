from script_api import *

f = AddByte("Function")

if f == 0: # available missions
    AddInt("count")
    AddInt("DungeonId")
elif f == 1: # finish dungeon mission
    AddInt("count") # ?
    # Dungeon mission class
    AddInt("DungeonId")
    AddShort("")
    AddShort("")
elif f == 2: # mission results
    count = AddInt("Count")
    for i in range(count):
        pass
elif f == 3: # finish dungeon
    AddBool("Unknown") # 1
