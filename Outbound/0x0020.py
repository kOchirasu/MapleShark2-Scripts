from script_api import *
from common import *

f = AddByte("function")

if f == 0: # StartSkill
    AddLong("SkillUseUid")
    AddInt("ServerTick")
    AddInt("SkillId")
    AddShort("SkillLevel") # 1? Skill Level?
    AddByte("AttackPoint") # +1 for each part of an attack
    DecodeCoordF("Position")
    DecodeCoordF("Direction")
    DecodeCoordF("Rotation")
    AddFloat("UnknownFloat")
    AddInt("ClientTick")
    AddBool("Unknown")
    AddLong("Unknown")
    b = AddBool("flag")
    if b:
        AddInt("Unknown")
        AddUnicodeString("Unknown")
elif f == 1: # Attacking?
    t = AddByte("AttackType")
    AddLong("SkillUseUid")
    if t == 0:
        AddByte("AttackPoint")
        DecodeCoordF("Position")
        DecodeCoordF("Direction")
        count = AddByte("count")
        AddInt("Unknown")
        for i in range(count):
            with Node("Npc " + str(i), True):
                AddInt("AttackCounter") # increments by 1 per attack
                AddInt("UserObjectId")
                AddInt("NpcObjectId")
                AddShort("AnimationFrame?")
    elif t == 1:
        AddInt("AttackCounter")
        AddInt("UserObjectId")
        DecodeCoordF("Position")
        DecodeCoordF("ImpactPosition")
        DecodeCoordF("Direction")
        AddByte("AttackPoint")
        count = AddByte("count")
        AddInt("Unknown")
        for i in range(count):
            with Node("Npc " + str(i), True):
                AddInt("NpcObjectId")
                AddByte("Unknown")
    elif t == 2:
        AddByte("Unknown")
        AddInt("Unknown")
        AddInt("Unknown")
        DecodeCoordF("Position")
        DecodeCoordF("Rotation")
elif f == 2: # charge skill
    AddLong("SkillUseUid")
    AddInt("SkillId")
    AddShort("SkillLevel")
    AddByte("MotionPoint")
    DecodeCoordF("Position")
    DecodeCoordF("Direction")
    DecodeCoordF("Rotation")
    DecodeCoordF("Unknown")
    AddByte("Unknown")
    AddByte("Unknown")
    AddInt("Unknown")
elif f == 3: # charging skill
    AddLong("SkillUseUid")
    AddInt("ServerTick")
elif f == 4: # Finish dash
    AddLong("SkillUseUid")
