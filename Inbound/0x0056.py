from script_api import *
from common import *

AddInt("ObjectId")
AddInt("NpcId")
DecodeCoordF("Position")
DecodeCoordF("Rotation")

# Dummy (not friendly and class >= 3)
#AddString("npcstring")

# If valid NpcId
with Node("Stats"):
    c = AddByte("Stats Flag") # 0x23
    if c == 1:
        v = AddByte("StatType")
        if v == 4: # Hp uses longs
            AddLong("TotalHp")
            AddLong("MinHp")
            AddLong("MaxHp")
        else:
            AddInt("TotalStat")
            AddInt("MinStat")
            AddInt("MaxStat")
    else:
        AddLong("TotalHp")
        AddInt("TotalAtkSpd")
        AddLong("MinHp")
        AddInt("MinAtkSpd")
        AddLong("MaxHp")
        AddInt("MaxAtkSpd")

AddBool("IsDead")
count = AddShort("Count")
for i in range(count):
    with Node("node " + str(i)):
        AddInt("NpcObjectId")
        AddInt("EffectObjectId")
        AddInt("NpcObjectId")
        DecodeAdditionalEffect()
        AddLong("AdditionalEffectRelated") # 0

AddLong("ItemUid") # From PetNpc
AddByte("Npc+6384")
AddInt("NpcLevel")
AddInt("Npc+1610")

# Dummy (not friendly and class >= 3)
"""AddUnicodeString("UnknownStr")
count = AddInt("Count")
for i in range(count):
    AddInt("SkillId")
    AddShort("SkillLevel")
AddInt("Unknown")"""

# Some flag condition on npc xml data
# AddLong("Npc+1620")

AddBool("Npc+6536")

"""
# AddString("ConditionedStrA")
# UnknownClassCall(packet)
AddByte("Unknown")
AddLong("Unknown")
AddByte("Unknown")
AddInt("Unknown")
AddInt("Unknown")
# Condition
AddString("UnknownStr")
count = AddInt("count")
for i in range(count):
    AddInt("Unknown")
    AddShort("Unknown")
AddInt("Unknown")
# EndCondition
# Condition
AddLong("Unknown")
# EndCondition
AddByte("Unknown")
"""
