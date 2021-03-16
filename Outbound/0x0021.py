from script_api import *

f = add_byte("function")
if f == 0:
    add_long("SkillUseUid")
    add_int("ServerTick")
    add_int("SkillId")
    add_short("Unknown")
    add_int("Animation")
    add_int("ClientTick")
    add_long("ItemUid")
