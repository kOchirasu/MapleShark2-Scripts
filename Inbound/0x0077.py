from script_api import *
from common import *

f = AddByte("Function")

if f == 0 or f == 1:
    AddString("EntityStrId")
    AddLong("SkillUseUid")
    AddInt("SkillId")
    AddShort("SkillLevel")
    AddByte("Unknown") # 1
    AddByte("Unknown") # 0
    DecodeCoordS("EntityRelated")
    AddInt("ServerTick")
    AddString("UnknownStr") # empty
    AddByte("Unknown") # 0
elif f == 2:
    AddString("UnknownStr")
    AddString("UnknownStr")
    AddByte("Unknown")
