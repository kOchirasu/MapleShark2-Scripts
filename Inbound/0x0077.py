from script_api import *
from common import *

f = add_byte("Function")

if f == 0 or f == 1:
    add_str("EntityStrId")
    add_long("SkillUseUid")
    add_int("SkillId")
    add_short("SkillLevel")
    add_byte("MotionPoint") # 1
    add_byte("AttackPoint") # 0
    decode_coordS("EntityRelated")
    add_int("ServerTick")
    add_str("UnknownStr") # empty
    add_byte("Unknown") # 0
elif f == 2:
    add_str("EntityStrId")
    add_str("UnknownStr")
    add_byte("Unknown")
