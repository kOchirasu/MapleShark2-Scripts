from script_api import *
from common import *

AddShort("Type")
count = AddByte("segments")
for i in range(count):
    DecodeSyncState()
AddInt("ClientTick")
AddInt("ServerTick")
