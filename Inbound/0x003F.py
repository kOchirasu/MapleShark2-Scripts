''' SKILL_SYNC '''
from script_api import *
from common import *

add_long("SkillCastId")
add_int("OwnerObjectId")
add_int("SkillId")
add_short("SkillLevel")
decode_coordF("Position")
decode_coordF("Direction")
decode_coordF("Rotation")
decode_coordF("Unknown")
add_byte("Unknown")
add_byte("AttackPoint")
add_int("Unknown")
