''' SKILL_USE_FAILED '''
from script_api import *

f = add_byte("function?")
add_long("SkillCastId")
add_int("ObjectId")
add_byte("Unknown")

if f == 5:
    pass # checks against state 16: gosPcSkill and SkillCastId
elif f == 6:
    add_int("PlayerState") # checks against specified state
add_int("Unknown")
add_short("CoordS / 10")
add_int("Unknown")
