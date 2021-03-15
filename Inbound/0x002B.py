from script_api import *
from common import *

AddInt("ObjectId")
id = AddInt("ItemId")
AddInt("Amount")
b = AddBool("Flag")
if b:
    AddLong("Uid")
DecodeCoordF("")
AddInt("LooterObjectId")
AddInt("Unknown")
AddByte("Unknown")
AddInt("Rarity")
AddShort("Unknown")
AddByte("Unknown")
AddByte("Unknown")
# No info for mesos...
if id != 90000001:
    DecodeItem(id)
