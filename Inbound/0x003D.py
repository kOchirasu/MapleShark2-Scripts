from script_api import *
from common import *

AddLong("SkillUseUid")
AddInt("ServerTick")
AddInt("ObjectId")
AddInt("SkillId")
AddShort("SkillLevel")
AddByte("MotionPoint")
DecodeCoordS("Position")
DecodeCoordF("Direction")
DecodeCoordF("Rotation")
AddShort("CoordS / 10")
AddBool("Unknown")
b = AddBool("Unknown")
if b:
    AddInt("Unknown")
    AddUnicodeString("Unknown")
