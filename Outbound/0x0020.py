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
    b = add_bool("flag")
    if b:
        add_int("Unknown")
        add_unicode_str("Unknown")
elif f == 1: # Attacking?
    t = add_byte("AttackType")
    add_long("SkillUseUid")
    if t == 0:
        add_byte("AttackPoint")
        decode_coordF("Position")
        decode_coordF("Direction")
        count = add_byte("count")
        add_int("Unknown")
        for i in range(count):
            with Node("Npc " + str(i), True):
                add_int("AttackCounter") # increments by 1 per attack
                add_int("UserObjectId")
                add_int("NpcObjectId")
                add_short("AnimationFrame?")
    elif t == 1:
        add_int("AttackCounter")
        add_int("UserObjectId")
        decode_coordF("Position")
        decode_coordF("ImpactPosition")
        decode_coordF("Direction")
        add_byte("AttackPoint")
        count = add_byte("count")
        add_int("Unknown")
        for i in range(count):
            with Node("Npc " + str(i), True):
                add_int("NpcObjectId")
                add_byte("Unknown")
    elif t == 2:
        add_byte("Unknown")
        add_int("Unknown")
        add_int("Unknown")
        decode_coordF("Position")
        decode_coordF("Rotation")
elif f == 2: # charge skill
    add_long("SkillUseUid")
    add_int("SkillId")
    add_short("SkillLevel")
    add_byte("MotionPoint")
    decode_coordF("Position")
    decode_coordF("Direction")
    decode_coordF("Rotation")
    decode_coordF("Unknown")
    add_byte("Unknown")
    add_byte("Unknown")
    add_int("Unknown")
elif f == 3: # charging skill
    add_long("SkillUseUid")
    add_int("ServerTick")
elif f == 4: # Finish dash
    add_long("SkillUseUid")
