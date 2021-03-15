from script_api import *
from common import *

f = AddByte("Function")
if f == 0:
    AddByte("type")
    AddInt("MountId")
    AddLong("Unknown") # 0
    AddLong("MountUid")
    DecodeUgcData()
elif f == 1:
    AddShort("Unknown") # 0
elif f == 2:
    AddInt("PlayerObjectId")
    AddInt("MountId")
    AddLong("MountUid")
