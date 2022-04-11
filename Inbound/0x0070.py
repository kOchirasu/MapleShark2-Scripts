from script_api import *
from common import *

f = add_byte("Function")
if f == 0: # Start (broadcast)
    n = add_short("Unknown+9")
    add_int("ObjectId")
    add_long("CharacterId")
    decode_coordF("Position")
    decode_coordF("Rotation?")
    if n == 0:
        add_long("Unknown")    # 1
elif f == 1: # End (broadcast)
    add_int("GuideObjectId")
    add_long("CharacterId")
elif f == 2: #sync (broadcast others)
    add_int("GuideObjectId")
    count = add_byte("segments")
    for i in range(count):
        decode_state_sync()
