from script_api import *
from common import *

f = AddByte("function")

if f == 0:
    AddLong("SkillUseUid")
    AddInt("ObjectId")
    AddInt("SkillId")
    AddShort("SkillLevel")
    AddByte("MotionPoint")
    AddByte("AttackPoint")
    DecodeCoordS("Impact")
    DecodeCoordF("ImpactDirection")
    AddByte("Unknown")
    AddInt("ServerTick")
    count = AddByte("count")
    for i in range(count):
        with Node("Node " + str(i)):
            AddLong("Unknown")
            AddInt("AttackCounter")
            AddInt("UserObjectId")
            AddInt("NpcObjectId")
            AddByte("Unknown")
            AddByte("Unknown")
elif f == 1:
    AddLong("SkillUseUid")
    AddInt("AttackCounter")
    AddInt("UserObjectId")
    AddInt("UserObjectId")
    AddInt("SkillId")
    AddShort("SkillLevel")
    AddByte("MotionPoint")
    AddByte("AttackPoint")
    DecodeCoordS("PositionOfImpact")
    DecodeCoordS("Direction")
    count = AddByte("count")
    for i in range(count):
        with Node("AttackedMonster " + str(i)):
            AddInt("MobObjectId")
            count2 = AddByte("Unknown")
            for j in range(count2):
                AddByte("Unknown")
                AddLong("Damage (neg)") # As negative
elif f == 3: # dot
    AddInt("OwnerId")
    AddInt("TargetId")
    AddInt("Tick")
    AddByte("DamageType")
    AddInt("Damage")
elif f == 4: # healing
    AddInt("CasterId")
    AddInt("TargetId")
    AddInt("???") # Some kind of counter?
    AddLong("MobHealth") # Healed amount
    AddInt("Unknown") # 0?
    AddByte("Unknown") # 1
elif f == 5: # region skill
    AddLong("Unknown")
    AddInt("UserObjectId")
    AddInt("SkillObjectId")
    AddByte("Unknown")
    count = AddByte("count")
    for i in range(count):
        with Node("Node " + str(i)):
            AddInt("PlayerObjectId")
            count2 = AddByte("Unknown")
            DecodeCoordS("BlockPosition")
            DecodeCoordF("Direction")
            for j in range(count2):
                AddByte("DanageType")
                AddLong("Damage")
elif f == 6: # tile skill
    AddLong("CastUid")
    AddInt("SkillId")
    AddShort("SkillLevel")
    count = AddByte("TargetCount")
    for i in range(count):
        with Node("Target " + str(i)):
            AddInt("PlayerObjectId")
            count2 = AddByte("Unknown")
            DecodeCoordS("Position")
            DecodeCoordF("Direction")
            for j in range(count2):
                AddByte("DamageType")
                AddLong("Damage")
elif f == 7:
    AddInt("Unknown")
    count = AddInt("count")
    for i in range(count):
        AddInt("Unknown")
elif f == 8:
    AddLong("Unknown")
    b = AddBool("Unknown")
    if b:
        AddInt("Unknown")
        AddShort("Unknown")
        AddInt("Unknown")
        AddInt("Unknown")
