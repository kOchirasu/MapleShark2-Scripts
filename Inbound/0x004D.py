from script_api import *
from common import *

f = AddByte("function")
AddInt("SkillObjectId?")
if f == 0:
    AddInt("OwnerObjectId") # this incremented on arrow rain
    AddInt("ServerTicks")
    count = AddByte("Count")
    for i in range(count):
        DecodeCoordF("Position")
    AddInt("SkillId")
    AddShort("SkillLevel")
    AddFloat("Unknown")
    AddFloat("Unknown")
