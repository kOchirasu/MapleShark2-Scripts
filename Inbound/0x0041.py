from script_api import *

f = add_byte("Function?")
add_long("SkillUseUid") # guess
add_int("ObjectId") # guess
add_byte("Unknown")

if f == 6:
    add_int("Unknown")
add_int("Unknown")
add_short("CoordS / 10")
add_int("Unknown")
