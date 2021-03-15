from script_api import *

f = AddByte("function")
if f == 0:
    AddLong("SkillUseUid")
    AddInt("ServerTick")
    AddInt("SkillId")
    AddShort("Unknown")
    AddInt("Animation")
    AddInt("ClientTick")
    AddLong("ItemUid")
