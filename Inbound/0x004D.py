from script_api import *
from common import *

f = add_byte("function")
add_int("SkillObjectId?")
if f == 0:
    add_int("OwnerObjectId") # this incremented on arrow rain
    add_int("ServerTicks")
    count = add_byte("Count")
    for i in range(count):
        decode_coordF("Position")
    add_int("SkillId")
    add_short("SkillLevel")
    add_float("Unknown")
    add_float("Unknown")
