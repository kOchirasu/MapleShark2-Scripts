from script_api import *

f = AddByte("function")
AddByte("Unknown") # 1

if f == 0: # close recall
    pass # none
elif f == 1: # open recall
    AddUnicodeString("PlayerName") # player who used the scroll
    AddInt("Unknown") # 1
    AddInt("MapId")
    AddInt("Unknown") # Random ticks? (Unknown)
    AddLong("Timestamp")
