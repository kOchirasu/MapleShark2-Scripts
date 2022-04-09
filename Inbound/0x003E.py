''' SKILL_DAMAGE '''
from script_api import *
from common import *

f = add_byte("function")

if f == 0:
    add_long("SkillCastId")
    add_int("OwnerObjectId")
    add_int("SkillId")
    add_short("SkillLevel")
    add_byte("MotionPoint")
    add_byte("AttackPoint")
    decode_coordS("ImpactPosition")
    decode_coordF("ImpactDirection")
    add_byte("Unknown")
    add_int("ServerTick")
    count = add_byte("TargetCount")
    for i in range(count):
        with Node("Target " + str(i)):
            add_long("Unknown")
            add_int("AttackCounter")
            add_int("OwnerObjectId")
            add_int("TargetObjectId")
            add_byte("State")
            add_byte("SubState")
elif f == 1:
    add_long("SkillCastId")
    add_int("AttackCounter")
    add_int("OwnerObjectId")
    add_int("OwnerObjectId")
    add_int("SkillId")
    add_short("SkillLevel")
    add_byte("MotionPoint")
    add_byte("AttackPoint")
    decode_coordS("ImpactPosition")
    decode_coordS("Direction")
    count = add_byte("TargetCount")
    for i in range(count):
        with Node("Target " + str(i)):
            add_int("TargetObjectId")
            count2 = add_byte("DamageCount")
            for j in range(count2):
                add_byte("Type")
                add_long("Damage") # As negative
elif f == 3: # dot
    add_int("OwnerObjectId")
    add_int("TargetObjectId")
    add_int("Tick")
    add_byte("DamageType")
    add_int("Damage")
elif f == 4: # healing
    add_int("OwnerObjectId")
    add_int("TargetObjectId")
    add_int("Tick") # Some kind of counter
    add_long("HpAmount")
    add_int("SpAmount")
    add_byte("EpAmount")
elif f == 5: # region skill
    add_long("SkillCastId") # 0 since this is from field
    add_int("UserObjectId")
    add_int("SkillObjectId")
    add_byte("AttackPoint") # guess
    count = add_byte("TargetCount")
    for i in range(count):
        with Node("Target " + str(i)):
            add_int("TargetObjectId")
            count2 = add_byte("DamageCount")
            decode_coordS("BlockPosition")
            decode_coordF("Direction")
            for j in range(count2):
                add_byte("Type")
                add_long("Damage")
elif f == 6: # tile skill
    add_long("SkillCastId")
    add_int("SkillId")
    add_short("SkillLevel")
    count = add_byte("TargetCount")
    for i in range(count):
        with Node("Target " + str(i)):
            add_int("TargetObjectId")
            count2 = add_byte("DamageCount")
            decode_coordS("Position")
            decode_coordF("Direction")
            for j in range(count2):
                add_byte("Damage")
                add_long("Damage")
elif f == 7:
    add_int("Unknown")
    count = add_int("count")
    for i in range(count):
        add_int("Unknown")
elif f == 8:
    add_long("SkillCastId")
    b = add_bool("Unknown")
    if b:
        add_int("Unknown")
        add_short("Unknown")
        add_int("Unknown")
        add_int("Unknown")
