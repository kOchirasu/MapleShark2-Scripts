from script_api import *
from item import *

f = add_byte("Function")
if f == 0:
    add_byte("type")
    add_int("MountId")
    add_long("Unknown") # 0
    add_long("MountUid")
    decode_ugc_item_look()
elif f == 1:
    add_short("Unknown") # 0
elif f == 2:
    add_int("PlayerObjectId")
    add_int("MountId")
    add_long("MountUid")
