from script_api import *
from common import *

AddByte("Function")
AddInt("ServerTick")
AddInt("ClientTicks")
count = AddByte("segments")
for i in range(count):
    with Node("Segment " + str(i), True):
        DecodeSyncState()
        AddInt("ClientTicks")
        AddInt("ServerTick")
