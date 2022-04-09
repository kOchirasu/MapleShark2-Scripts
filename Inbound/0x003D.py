''' SKILL_USE '''
from script_api import *
from common import *

add_long("SkillUseUid")
add_int("ServerTick")
add_int("ObjectId")
add_int("SkillId")
add_short("SkillLevel")
add_byte("MotionPoint")
decode_coordS("Position")
decode_coordF("Direction")
decode_coordF("Rotation")
add_short("CoordS / 10")
add_bool("Unknown")
b = add_bool("Unknown")
if b:
    add_int("Unknown")
    add_unicode_str("Unknown")
