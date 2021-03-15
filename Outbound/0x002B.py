from script_api import *

f = AddByte("function")
if f == 1: # Reset dungeon
    pass # none
elif f == 2: # Enter Dungeon (HArd Rog)
    AddInt("DungeonRoomId")
    AddBool("WithParty")
    AddInt("Unknown")
    AddByte("Unknown") # 0 const?
elif f == 3:
    AddInt("Unknown")
elif f == 4:
    pass # none
elif f == 8:
    AddInt("Unknown")
    AddLong("Unknown") # Maybe int/int
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
    AddInt("Unknown")
elif f == 17:
    AddInt("Unknown")
elif f == 18:
    AddInt("Unknown")
elif f == 22:
    pass # none
elif f == 25:
    AddInt("Unknown")
    AddByte("Unknown") # bool?
