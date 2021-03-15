from script_api import *

# dungeon title id
# dungeon goal id
# fame challenge dungeon...?
f = AddByte("Function")
if f == 1:
    pass # unknown
elif f == 2:
    AddByte("Unknown")
    AddInt("Unknown")
else:
    count = AddInt("count")
    for i in range(count):
        with Node("DungeonRoom " + str(i)):
            AddInt("Id")
            AddByte("Unknown") # Eligible?
