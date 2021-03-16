from script_api import *

f = add_byte("function")
if f == 1: # Reset dungeon
    pass # none
elif f == 2: # Enter Dungeon (HArd Rog)
    add_int("DungeonRoomId")
    add_bool("WithParty")
    add_int("Unknown")
    add_byte("Unknown") # 0 const?
elif f == 3:
    add_int("Unknown")
elif f == 4:
    pass # none
elif f == 8:
    add_int("Unknown")
    add_long("Unknown") # Maybe int/int
elif f == 9:
    pass # none
elif f == 10: # enter rog dungeon portal
    pass # none
elif f == 13:
    pass # none
elif f == 14:
    pass # none
elif f == 15:
    pass # none
elif f == 16:
    add_int("Unknown")
elif f == 17:
    add_int("Unknown")
elif f == 18:
    add_int("Unknown")
elif f == 22:
    pass # none
elif f == 25:
    add_int("Unknown")
    add_byte("Unknown") # bool?
