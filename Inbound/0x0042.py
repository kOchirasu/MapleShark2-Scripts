''' STATE_SKILL '''
from script_api import *

f = add_byte("Function")
if f == 6:
    add_int("OwnerObjectId")
    add_long("SkillCastId")
    add_int("SkillId")
    add_int("Animation")
    # add_int("ServerTick") server might send this, but it's ignored
