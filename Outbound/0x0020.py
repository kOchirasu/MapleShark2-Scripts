from script_api import *
from common import *

f = add_byte("function")

if f == 0: # StartSkill
    add_long("SkillUseUid")
    add_int("ServerTick")
    add_int("SkillId")
    add_short("SkillLevel") # 1? Skill Level?
    add_byte("AttackPoint") # +1 for each part of an attack
    decode_coordF("Position")
    decode_coordF("Direction")
    decode_coordF("Rotation")
    add_float("UnknownFloat")
    add_int("ClientTick")
    add_bool("Unknown")
    add_long("Unknown")
    b = add_bool("IsHoldSkill") # HoldSkill
    if b:
        add_int("Unknown")
        add_unicode_str("Unknown")
elif f == 1: # Attacking?
    t = add_byte("AttackType")
    if t == 0:
        add_long("SkillUseUid")
        add_byte("AttackPoint")
        decode_coordF("Position")
        decode_coordF("Direction")
        count = add_byte("count")
        add_int("HoldCount")
        for i in range(count):
            with Node("Target " + str(i), True):
                add_long("SkillTargetUid")
                #add_int("AttackCounter") # increments by 1 per attack
                #add_int("CasterId")
                add_int("TargetId")
                add_byte("Index")
                while True:
                    b = add_bool("HasNextChain")
                    if not b:
                        break
                    with Node("TargetChain", True):
                        add_long("SkillTargetUid")
                        #add_int("AttackCounter")
                        #add_int("CasterId")
                        add_int("ChainTargetId")
                        add_byte("Index")
                        add_byte("unk2")
    elif t == 1:
        add_long("SkillUseUid")
        add_long("SkillTargetUid")
        #add_int("AttackCounter")
        #add_int("CasterId")
        decode_coordF("ImpactPosition1")
        decode_coordF("ImpactPosition2")
        decode_coordF("Direction|Rotation")
        add_byte("AttackPoint")
        count = add_byte("count")
        add_int("Unknown")
        for i in range(count):
            with Node("Target " + str(i), True):
                add_int("TargetObjectId")
                add_byte("Unknown")
    elif t == 2:
        add_long("SkillUseUid")
        add_byte("AttackPoint")
        add_int("Unknown")
        add_int("Unknown")
        decode_coordF("CastPosition")
        decode_coordF("CastRotation")
elif f == 2: # charge skill
    add_long("SkillUseUid")
    add_int("SkillId")
    add_short("SkillLevel")
    add_byte("MotionPoint")
    decode_coordF("Position")
    decode_coordF("Direction")
    decode_coordF("Rotation")
    decode_coordF("Unknown")
    add_bool("IsCharge")
    add_bool("IsRelease")
    add_int("Unknown")
elif f == 3: # charging skill
    add_long("SkillUseUid")
    add_int("ServerTick")
elif f == 4: # Finish dash
    add_long("SkillUseUid")
