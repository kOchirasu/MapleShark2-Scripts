from script_api import *
from common import *

f = add_byte("Function")
if f == 0: # start riding
    add_int("PlayerObjectId")
    mountType = add_byte("type")
    add_int("MountId")
    add_int("MountObjectId?")
    if mountType == 1:
        add_int("MountId")
        add_long("MountUid")
        # UGC Packet data
        decode_ugc_data()
    elif mountType == 2:
        add_int("Unknown+22")
        add_short("Unknown+26")
elif f == 1: # stop riding
    add_int("PlayerObjectId")
    add_short("0?")
elif f == 2:
    add_int("PlayerObjectId")
    add_int("MountId")
    add_long("MountUid")
elif f == 3:
    add_int("Unknown+9")
    add_int("Unknown+13")
    add_byte("Unknown+17")
    # ...
