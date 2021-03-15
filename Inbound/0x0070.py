from script_api import *
from common import *

f = AddByte("Function")
if f == 0: # Start (broadcast)
    n = AddShort("Unknown+9")
    AddInt("ObjectId")
    AddLong("CharacterId")
    DecodeCoordF("Position")
    DecodeCoordF("Rotation?")
    if n == 0:
        AddLong("Unknown")    # 1
elif f == 1: # End (broadcast)
    AddInt("GuideObjectId")
    AddLong("CharacterId")
elif f == 2: #sync (broadcast others)
    AddInt("GuideObjectId")
    count = AddByte("segments")
    for i in range(count):
        DecodeSyncState()
