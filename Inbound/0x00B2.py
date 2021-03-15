from script_api import *

f = AddByte("Function")
if f == 0: # world boss spawn map
    AddInt("BossMonsterId")
    AddInt("MapId")
    AddShort("Channel?")
    AddLong("Timestamp")
    AddBool("Alive?") # 1
