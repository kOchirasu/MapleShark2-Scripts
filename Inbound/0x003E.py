from script_api import *
from common import *

f = add_byte("function")

if f == 0:
    add_long("SkillUseUid")
    add_int("ObjectId")
    add_int("SkillId")
    add_short("SkillLevel")
    add_byte("MotionPoint")
    add_byte("AttackPoint")
    decode_coordS("Impact")
    decode_coordF("ImpactDirection")
    add_byte("Unknown")
    add_int("ServerTick")
    count = add_byte("count")
    for i in range(count):
        with Node("Node " + str(i)):
            add_long("Unknown")
            add_int("AttackCounter")
            add_int("UserObjectId")
            add_int("NpcObjectId")
            add_byte("Unknown")
            add_byte("Unknown")
elif f == 1:
    add_long("SkillUseUid")
    add_int("AttackCounter")
    add_int("UserObjectId")
    add_int("UserObjectId")
    add_int("SkillId")
    add_short("SkillLevel")
    add_byte("MotionPoint")
    add_byte("AttackPoint")
    decode_coordS("PositionOfImpact")
    decode_coordS("Direction")
    count = add_byte("count")
    for i in range(count):
        with Node("AttackedMonster " + str(i)):
            add_int("MobObjectId")
            count2 = add_byte("Unknown")
            for j in range(count2):
                add_byte("Unknown")
                add_long("Damage (neg)") # As negative
elif f == 3: # dot
    add_int("OwnerId")
    add_int("TargetId")
    add_int("Tick")
    add_byte("DamageType")
    add_int("Damage")
elif f == 4: # healing
    add_int("CasterId")
    add_int("TargetId")
    add_int("???") # Some kind of counter?
    add_long("MobHealth") # Healed amount
    add_int("Unknown") # 0?
    add_byte("Unknown") # 1
elif f == 5: # region skill
    add_long("Unknown")
    add_int("UserObjectId")
    add_int("SkillObjectId")
    add_byte("Unknown")
    count = add_byte("count")
    for i in range(count):
        with Node("Node " + str(i)):
            add_int("PlayerObjectId")
            count2 = add_byte("Unknown")
            decode_coordS("BlockPosition")
            decode_coordF("Direction")
            for j in range(count2):
                add_byte("DanageType")
                add_long("Damage")
elif f == 6: # tile skill
    add_long("CastUid")
    add_int("SkillId")
    add_short("SkillLevel")
    count = add_byte("TargetCount")
    for i in range(count):
        with Node("Target " + str(i)):
            add_int("PlayerObjectId")
            count2 = add_byte("Unknown")
            decode_coordS("Position")
            decode_coordF("Direction")
            for j in range(count2):
                add_byte("DamageType")
                add_long("Damage")
elif f == 7:
    add_int("Unknown")
    count = add_int("count")
    for i in range(count):
        add_int("Unknown")
elif f == 8:
    add_long("Unknown")
    b = add_bool("Unknown")
    if b:
        add_int("Unknown")
        add_short("Unknown")
        add_int("Unknown")
        add_int("Unknown")
