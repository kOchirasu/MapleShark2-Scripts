from script_api import *

# dungeon title id
# dungeon goal id
# fame challenge dungeon...?
f = add_byte("Function")
if f == 1:
    pass # unknown
elif f == 2:
    add_byte("Unknown")
    add_int("Unknown")
else:
    count = add_int("count")
    for i in range(count):
        with Node("DungeonRoom " + str(i)):
            add_int("Id")
            add_byte("Unknown") # Eligible?
