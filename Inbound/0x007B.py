from script_api import *
from common import *

f = AddByte("Function")
if f == 0: # start riding
    AddInt("PlayerObjectId")
    mountType = AddByte("type")
    AddInt("MountId")
    AddInt("MountObjectId?")
    if mountType == 1:
        AddInt("MountId")
        AddLong("MountUid")
        # UGC Packet data
        DecodeUgcData()
    elif mountType == 2:
        AddInt("Unknown+22")
        AddShort("Unknown+26")
elif f == 1: # stop riding
    AddInt("PlayerObjectId")
    AddShort("0?")
elif f == 2:
    AddInt("PlayerObjectId")
    AddInt("MountId")
    AddLong("MountUid")
elif f == 3:
    AddInt("Unknown+9")
    AddInt("Unknown+13")
    AddByte("Unknown+17")
    # ...
